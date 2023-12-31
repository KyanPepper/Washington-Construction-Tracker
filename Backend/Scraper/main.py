from Scraper.counties.snohomishcounty import scrapesnohomish
from Scraper.WS.wsMajor import scrapeWsMajor
from Scraper.WS.lightRail import scrapelightrail
def scrape_all():

    all_projects = []

    all_projects.extend(scrapesnohomish())
    all_projects.extend(scrapeWsMajor())
    all_projects.extend(scrapelightrail())
    
    return all_projects

    
