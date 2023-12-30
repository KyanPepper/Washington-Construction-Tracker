#this file calls other functions
from bs4 import BeautifulSoup
import requests 
import re
import pprint
from counties.snohomishcounty import scrapesnohomish
from WS.wsMajor import scrapeWsMajor
from WS.lightRail import scrapelightrail

all_projects = []

all_projects.extend(scrapesnohomish())
all_projects.extend(scrapeWsMajor())
all_projects.extend(scrapelightrail())
pprint.pprint(all_projects)
