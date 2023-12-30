from bs4 import BeautifulSoup
import requests 
import re
def scrapesnohomish():

    projects = []

    url = 'https://snohomishcountywa.gov/3599/Current-Construction-Projects'
    broadurl = 'https://snohomishcountywa.gov/'
    doc = requests.get(url)
    thedoc = BeautifulSoup(doc.text,'html.parser')
    #print(thedoc)
    navbar = thedoc.find('ol',id = 'secondaryMenusecondaryNav')
    #print(navbar.prettify())
    links = navbar.find_all('a' , class_ = 'navMainItem')
    #print(links)
    for link in links:
        href = broadurl + link.get('href')
        location = link.get_text(strip=True)
        location = re.sub(r'\s*\(\d{4}\)', '', location)
        newdoc = requests.get(href)
        projurl = href
        thenewdoc = BeautifulSoup(newdoc.text, 'html.parser')
        title = thenewdoc.find('h1').get_text(strip=True)
        newdiv = thenewdoc.find('div', class_ = 'pageStyles')
        description = newdiv.find('p').get_text(strip=True)
        price = newdiv.find('h2',string='Funding').find_next('p').get_text(strip=True)
        timeline = newdiv.find('h2',string='Schedule').find_next('p').get_text(strip=True)
        tempimg = thenewdoc.find_all('img')
        if '14666' not in tempimg[4].get('src'):
            img = broadurl + tempimg[4].get('src')
        else:
            img =broadurl + tempimg[3].get('src')

        project ={
                'name' : title,
                'img' : img,
                'url' : projurl,
                'price' : price,
                'timeline' : timeline,
                'description' : description,
                'location' : location
        }
        projects.append(project)
        print(title)
    return projects

        
    
        

        