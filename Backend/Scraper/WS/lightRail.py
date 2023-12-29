from bs4 import BeautifulSoup
import requests 

def lightrailscrape():
    projects = []

    url = 'https://en.wikipedia.org/wiki/Link_light_rail'
    broadurl = 'https://en.wikipedia.org'
    result = requests.get(url)
    doc = BeautifulSoup(result.text,'html.parser')
    img = doc.find('figure',class_ = 'mw-default-size').find('img').get('src')
    price = '$131 billion (Total)'
    wikitable = doc.find('div', class_ = 'mw-content-ltr mw-parser-output')

    wikitable = wikitable.find('table', class_='wikitable')
    rows = wikitable.find_all('tr')[1:]
    #iterates through first column

    for row in rows:
        cells = row.find_all(['th', 'td'])
        url = broadurl + cells[0].find('a').get('href')
        title = cells[0].find('a').get_text(strip = True)
        description = cells[2].contents[0].strip()
        location = cells[3].find('a').get_text(strip = True)
        timeline = '2003 - ' + cells[7].contents[0].strip()
        project ={
                'name' : title,
                'img' : img,
                'url' : url,
                'price' : price,
                'timeline' : timeline,
                'description' : description,
                'location' : location
        }
        projects.append(project)
    
    return projects