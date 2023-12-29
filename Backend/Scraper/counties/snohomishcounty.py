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
        location = link.get_text()
        location = re.sub(r'\s*\(\d{4}\)', '', location)
        newdoc = requests.get(href)
        projurl = href
        thenewdoc = BeautifulSoup(newdoc.text, 'html.parser')
        title = thenewdoc.find('h1').get_text()
        newdiv = thenewdoc.find('div', class_ = 'pageStyles')
        description = newdiv.find('p').get_text()
        price = newdiv.find('h2',string='Funding').find_next('p').get_text()
        timeline = newdiv.find('h2',string='Funding').find_next('p').get_text()
        tempimg = thenewdoc.find_all('img')
        if '14666' not in tempimg[4].get('src'):
            img = tempimg[4].get('src')
        else:
            img =tempimg[3].get('src')

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
    
        
    
        

        