
import requests
from bs4 import BeautifulSoup as Bs


URL = "https://en.wikipedia.org/wiki/Lists_of_films"
response = requests.get(URL)
soup = Bs(response.text, "html.parser")

headers_items = soup.find_all('div', class_="mw-heading mw-heading3")

start = 0
for ind, item in enumerate(headers_items):
    if item.find('h3')['id'] == "Historical":
        start = ind

for item in headers_items[start:]:
    list_of_titles = item.next_sibling.next_sibling
    for ul in list_of_titles.find_all('li'):
        title = ul.find('a').text
        link = ul.find('a')['href']
        print(f"Заголовок - {title}, ссылка =- https://en.wikipedia.org{link}")
    if item.next_sibling.next_sibling.next_sibling.next_sibling['class'][1] == 'mw-heading2':
        break