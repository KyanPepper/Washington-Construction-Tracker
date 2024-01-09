from Scraper.counties.snohomishcounty import scrapesnohomish
from Scraper.WS.wsMajor import scrapeWsMajor
from Scraper.WS.lightRail import scrapelightrail
def scrape_all():

    all_projects = []

    
    all_projects.extend(scrapeWsMajor())
    all_projects.extend(scrapelightrail())
    all_projects.extend(scrapesnohomish())
    
    return all_projects

    
