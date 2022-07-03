
from bs4 import BeautifulSoup
import requests


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

    date_published = sub_soup.find('div', class_='news-article__about').p['content']
    print(date_published)

    category = sub_soup.find('div', class_='news-article__breadcrumbs').a.get_text()










