from bs4 import BeautifulSoup
import requests

url = 'https://www.piercecountywa.gov/507/Construction-Projects'
result = requests.get(url)
doc = BeautifulSoup(result.content, 'html.parser')

widget_body = doc.find('div', class_='widgetBody')  
print(doc.prettify())
