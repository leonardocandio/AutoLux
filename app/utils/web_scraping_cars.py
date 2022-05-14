import requests
from bs4 import BeautifulSoup
from sqlalchemy import null
    
def create_all_cars(db, Car):
    brands = generate_brands()
    cars = generate_cars(brands)
    i=0
    for car in cars.values():
        try:
            name = car['name']
            image_url = car["img_url"]
            price = car['price']
            description = car['description']
            brand = car['Marca']
            model = car['Modelo']
            category = car['Categoría']
            year = car['Año de modelo']
            year_production = car['Año de fabricación']
            mileage = car['Kilometraje']
            transmission = car['Tipo de transmisión']
            fuel = car['Combustible']
            engine_displacement = car['Cilindrada (cc)']
            doors = car['Número de puertas']
            drivetrain = car['Tracción']
            color = car['Color']
            cylinders = car['Número de cilindros']
            location = car['Ubicación']

            new_car = Car(
                name=name,
                image_url=image_url,
                price=price,
                description=description,
                brand=brand,
                model=model,
                category=category,
                year=year,
                year_production=year_production,
                mileage=mileage,
                transmission=transmission,
                fuel=fuel,
                engine_displacement=engine_displacement,
                doors=doors,
                drivetrain=drivetrain,
                color=color,
                cylinders=cylinders,
                location=location
            )
            db.session.add(new_car)
            db.session.commit()
            i += 1
            print(i, " Added")
        except Exception as e:
            print(e)
            db.session.rollback()
        finally:
            db.session.close()
            

def create_all_brands(db, Brand):
    brands = generate_brands()
    for brand in brands.values():
        try:
            new_brand = Brand(
            name=brand['name'],
            image_url=brand['image_url']
            )
            db.session.add(new_brand)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
        finally:
            db.session.close()
            

def generate_brands():
    brands = {}
    s0 = requests.Session()
    r1 = requests.get("https://neoauto.com/")

    if r1.status_code == 200:
        soup = BeautifulSoup(r1._content.decode(), "html.parser")

        div_brands = soup.find('div', {'class': "tab_marca active"})
        lis = div_brands.find_all('li')

        for li in lis:
            brand_name = li.find('img')['alt']
            brand_image_url = li.find_all('img')[1]['src']
            url = li.find('a')['href']
            
            brands[brand_name] = {}
            brands[brand_name]['name'] = brand_name
            brands[brand_name]['image_url'] = brand_image_url
            brands[brand_name]['url'] = url
        s0.close()

    return brands


def generate_cars(brands):
    cars = {}
    for value in brands.values():
        s1 = requests.Session()
        r = s1.get(value['url'])
  
        if r.status_code == 200:
            soup = BeautifulSoup(r._content.decode(), "html.parser")
            div_results = soup.find('div', {'class': 's-results js-container'})
            all_a = div_results.find_all('a', {'class', 'c-results-use__link'})

            # Se agregan todos las url de los carros de esa marca
            cars_urls = [a['href'] for a in all_a]
            s1.close()

            for url in cars_urls:
                s2 = requests.Session()
                req_car = s2.get("https://neoauto.com/" + url)
                if req_car.status_code == 200:
                    soup_car = BeautifulSoup(req_car._content.decode(), "html.parser")

                    header = soup_car.find('header', {'class': 'title-info'})
                    name = header.find('h1',{'class':'title'}).text

                    div_img = soup_car.find_all('article')[0]
                    # print(div_img)
                    figure_img = div_img.find('figure')
                    img_url = figure_img.find('img')['data-lazy']

                    price = soup_car.find('p', {'class': 'price title-info__price'}).text[4:]
                    price = price.replace(',', "")
                    try:
                        price = int(price)
                    except Exception as e:
                        price = 0

                    description = soup_car.find('div', {'class': "ficha_descripcion js-container-description"})
                    if description is not None:
                        description = description.find('p').text

                    #Voy a usar el url como identificar para cada carro
                    cars[url] = {}
                    cars[url]["name"] = name
                    cars[url]["img_url"] = img_url
                    cars[url]["price"] = price
                    cars[url]["description"] = description
                    
                    section = soup_car.find('section', {'class': 'feature feature_first'})
                    trs = section.find_all("tr")
                    
                    for tr in trs:
                        ths = tr.find_all("th")
                        field = ths[0].text
                        val = ths[1].text
                        if field == "Año de modelo" or field == "Kilometraje" or field == "Año de fabricación" or field == "Año de fabricación" or field == "Número de puertas" or field == "Número de cilindros":
                            try:
                                val = int(val)
                            except Exception as e:
                                val = 0
                        if field == "Marca" or field == "Modelo":
                            if field == None:
                                print("No Marca o Modelo")
                                break

                        cars[url][field] = val
                    s2.close()
        else:
            print("No se logro ingresar a la url ")

    return cars
