from bs4 import BeautifulSoup
import requests 

def scrapeWsMajor():
    projects = []

    broadUrl = 'https://wsdot.wa.gov'
    url = "https://wsdot.wa.gov/construction-planning/major-projects"

    result = requests.get(url)
    doc = BeautifulSoup(result.text,"html.parser")
    #div containing main projects
    viewstring = 'view-content'
    view_content_div = doc.find("div", class_="view-content")
    #print(view_content_div.prettify())

    if view_content_div:
        links = view_content_div.find_all("a", href=True)

        #subpage links for major projects
        for link in links:
            #finds href within the link
            href = link.get("href")  
            newUrl = broadUrl+href
        
            #print(newUrl)
            subresult = requests.get(newUrl)
            subDoc = BeautifulSoup(subresult.text,"html.parser")
            #grab title
            title = subDoc.find("h1" ).find('span').get_text(strip=True)
            subcontentdiv = subDoc.find("div",class_ ="content")
            #print(subcontentdiv.prettify())
            #Grab piclink
            piclink = broadUrl + subcontentdiv.find('img').get("src")
            #grab desciption
            description = subcontentdiv.find('p').get_text(strip=True)
            #grab timeline etc..
            timeline = subcontentdiv.find('div',class_ = 'field field--name-field-timeline-overview-project field--type-string field--label-hidden field--item').get_text(strip=True)
            price = subcontentdiv.find('div', class_ = 'field field--name-field-funding field--type-string field--label-hidden field--item').getText(strip=True)
            location = extract_from_title(title)
            project ={
                'name' : title,
                'img' : piclink,
                'url' : newUrl,
                'price' : price,
                'timeline' : timeline,
                'description' : description,
                'location' : location
            }
            

            projects.append(project)

    else:
        print('accsess blocked :( ')
    return projects

def extract_from_title(title):
    keywords = ['I-5', 'I-90', 'SR 167', 'SR 160', 'SR 522', 'SR 512', 'SR 520', 'SR 525', 'SR 529', 'Snoqualmie', 'Bellevue', 'Seattle', 'Tacoma', 'Everett', 'Kirkland', 'Spokane', 'Puget Sound', 'I-405', 'SR 18', 'SR 202', 'SR 99', 'SR 9']
    locations = []

    title_lower = title.lower()
    for keyword in keywords:
        if keyword.lower() in title_lower:
            locations.append(keyword.replace('-', ' '))

    return ' '.join(locations) + ' Washington' if locations else None
