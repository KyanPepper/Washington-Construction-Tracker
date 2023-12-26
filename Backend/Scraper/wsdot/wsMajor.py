from bs4 import BeautifulSoup
import requests 

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
        print(href)
else:
    print('accsess blocked :( ')