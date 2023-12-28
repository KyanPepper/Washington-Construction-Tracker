from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = 'https://www.piercecountywa.gov/507/Construction-Projects'

# Launch a headless browser using Selenium
options = webdriver.ChromeOptions()
options.add_argument('headless')  # Run Chrome in headless mode
driver = webdriver.Chrome(options=options)  # You might need to provide the path to your WebDriver executable

driver.get(url)

# Let the page load
time.sleep(5)  # Adjust the sleep time based on the page load speed

# Get the page source after it's been dynamically loaded
html_content = driver.page_source

# Use Beautiful Soup to parse the content
doc = BeautifulSoup(html_content, 'html.parser')

# Continue with your scraping logic
# ...

# Close the browser session
driver.quit()
