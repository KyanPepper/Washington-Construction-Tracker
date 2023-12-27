from bs4 import BeautifulSoup
import requests 

projects = []

url = 'https://www.piercecountywa.gov/507/Construction-Projects'

result = requests.get(url)
doc = BeautifulSoup(result.text,'html.parser')

item = doc.find('div', class_ ='widgetBody')
print(item.prettify())