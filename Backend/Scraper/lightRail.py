from bs4 import BeautifulSoup
import requests 

projects = []

url = 'https://en.wikipedia.org/wiki/Link_light_rail'

result = requests.get(url)
doc = BeautifulSoup(result.text,'html.parser')
wikitable = doc.find('div', class_ = 'mw-content-ltr mw-parser-output')
wikitable = wikitable.find('table', class_='wikitable')
rows = wikitable.find_all('tr')
for row in rows:
    first_box = row.find('th') 
    if first_box:
        print(first_box.text.strip())
