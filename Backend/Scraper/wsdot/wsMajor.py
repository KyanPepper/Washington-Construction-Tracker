from bs4 import BeautifulSoup
import requests 

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
        subcontentdiv = subDoc.find("div",class_ ="content")
        #print(subcontentdiv.prettify())
        #search throught text
        pic = subcontentdiv.find('img src')
        print(pic)

        break

else:
    print('accsess blocked :( ')

