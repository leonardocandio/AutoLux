from datetime import datetime
from bs4 import BeautifulSoup
import requests


def create_all_articles(db, Article):
    # Buscamos los articulos que vamos a usar
    r = requests.get("https://noticias.autocosmos.com.pe/listado")

    #Añadimos el url de cada noticia a la lista
    url_all_news = []

    soup = BeautifulSoup(r._content, 'html.parser')
    articles = soup.find_all('article')

    for article in articles:
        url_all_news.append(article.find_all('a')[1]['href'])


    # Cada notica tiene title, description, content, image_url, author, date_published, category
    # Recuperamos los html de todas las noticas
    for url in url_all_news:
        sub_r = requests.get(url)

        sub_soup = BeautifulSoup(sub_r._content, 'html.parser')

        title = sub_soup.h1.get_text()

        description = sub_soup.h2.get_text()

        image_url = sub_soup.picture.img['src']

        ps = sub_soup.find(id='newsText').find_all('p', string=True)
        content = ''
        for p in ps:
            content += p.get_text() + "\n\n"

        author = sub_soup.find('div', class_='news-article__about').span.get_text()

        date_raw = sub_soup.find('div', class_='news-article__about').p['content']
        date_published = datetime.strptime(date_raw, '%Y-%m-%d')

        category = sub_soup.find('div', class_='news-article__breadcrumbs').a.get_text()

        try:
            # Creamos cada articulo de noticia y lo añadimos a la base de datos
            article = Article(
                title= title,
                description = description,
                image_url= image_url,
                content= content,
                author= author,
                date_published= date_published,
                category= category
            )
            db.session.add(article)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
        finally:
            db.session.close()