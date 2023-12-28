from bs4 import BeautifulSoup
import requests 

projects = []

url = 'https://snohomishcountywa.gov/3599/Current-Construction-Projects'
doc = requests.get(url)
thedoc = BeautifulSoup(doc.text,'html.parser')
#print(thedoc)
navbar = thedoc.find('ol',id = 'secondaryMenusecondaryNav')
#print(navbar.prettify())
links = navbar.find_all('a' , class_ = 'navMainItem')
#print(links)

    