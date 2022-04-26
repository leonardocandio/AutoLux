import requests
import json
    
def create_all_cars(db, Car):
    response = requests.get("https://private-anon-f47bd87479-carsapi1.apiary-mock.com/cars")
    cars = json.loads(response.text)

    for car in cars:
        year = car["year"]
        make = car["make"]
        model = car["model"]
        horse_power = car["horsepower"]
        price = car["price"]
        image_url = car["img_url"]
        name = make + " " + model + " " + str(year)

        car = Car(
            name=name,
            make=make,
            model=model,
            image_url=image_url,
            year=year,
            horse_power=horse_power,
            price=price
        )

        db.session.add(car)
        db.session.commit()
    

# import requests

# url = "https://car-data.p.rapidapi.com/cars"

# querystring = {"limit":"50","page":"0"}

# headers = {
# 	"X-RapidAPI-Host": "car-data.p.rapidapi.com",
# 	"X-RapidAPI-Key": "a3af21f153msh082cc63b3aecc7cp1e3222jsn1c0b907ce263"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)