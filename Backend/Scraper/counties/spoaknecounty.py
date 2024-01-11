from bs4 import BeautifulSoup
import requests 
import re
non_address_keywords = [
    "Roundabout", "-" "Replacement", "Project", "Intersection", "Improvement", "Route", "Widening",
    "Signing", "Bank", "Stabilization", "School", "SRTS", "Culvert", "Passage", "Drainage",
    "Bridge", "Elementary", "Fish", "Sewer", "MP", "Phase", "Terrace", "Bike", "Curve", "Market","Culvert","Rail", "No."
]

def clean_address(text):
    cleaned_text = text
    for keyword in non_address_keywords:
        cleaned_text = re.split(r'\b{}\b'.format(re.escape(keyword)), cleaned_text, flags=re.IGNORECASE)[0].strip()
    return cleaned_text


def scrapeSpokane():
    projects = []
    url = 'https://www.spokanecounty.org/805/Current-Projects'
    broadurl = 'https://www.spokanecounty.org/'
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
            location_parts = location.split('-')
            if len(location_parts) > 0:
                location = location_parts[0]
                
                location = clean_address(location)
                location += ' Spokane'
                newdoc = requests.get(href)
                projurl = href
                thenewdoc = BeautifulSoup(newdoc.text, 'html.parser')
                title = thenewdoc.find('h1').get_text(strip=True)
                newdiv = thenewdoc.find('div', class_ = 'moduleContentNew')
                newdiv = newdiv.find('div', class_ = 'fr-view')
            #   print(newdiv)
                timeline = description = funding = None
                for tag in newdiv.find_all('p'):
                    text = tag.get_text(strip=True)
                    if 'Timeline:' in text:
                        timeline = text.split(':')[-1].strip()
                    elif 'Description:' in text:
                        description = text.split(':')[-1].strip()
                    elif 'Funding:' in text:
                        funding = text.split(':')[-1].strip()

                if newdiv.find('img') != None:
                    img = broadurl + newdiv.find('img').get('src')
                else:
                    img = 'src\\lib\\notfoundlogo.jpg'
                project ={
                    'name' : title,
                    'img' : img,
                    'url' : projurl,
                    'price' : funding,
                    'timeline' : timeline,
                    'description' : description,
                    'location' : location,
                    'county' : 'Spokane County'
                }
                projects.append(project)
    return projects