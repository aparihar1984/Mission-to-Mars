# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup

import pandas as pd

# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path)

# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# Setting up the HTML Parser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('ul.item_list li.slide')

slide_elem.find("div", class_='content_title')

# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p

# ### Featured Images

# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()

# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url

df = pd.read_html('http://space-facts.com/mars/')[0]
df.columns=['description', 'value']
df.set_index('description', inplace=True)
df

df.to_html()

browser.quit()

# Import Splinter, BeautifulSoup, and Pandas.  Deliverable 1 Challenge starts with adding the starter code to the module code.
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd

# Path to chromedriver
get_ipython().system('which chromedriver')

# Set the executable path and initialize the chrome browser in splinter
executable_path = {'executable_path': 'chromedriver'}
browser = Browser('chrome', **executable_path)

# ### Visit the NASA Mars News Site

# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')

slide_elem.find("div", class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p

# ### JPL Space Images Featured Image

# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_id('full_image')
full_image_elem.click()

# Find the more info button and click that
browser.is_element_present_by_text('more info', wait_time=1)
more_info_elem = browser.links.find_by_partial_text('more info')
more_info_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# find the relative image url
img_url_rel = img_soup.select_one('figure.lede a img').get("src")
img_url_rel

# Use the base url to create an absolute url
img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
img_url

# ### Mars Facts

df = pd.read_html('http://space-facts.com/mars/')[0]

df.head()

df.columns=['Description', 'Mars']
df.set_index('Description', inplace=True)
df

df.to_html()

# ### Mars Weather

# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)

# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')

# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())

# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# 1. Use browser to visit the URL, and visiting the quotes to scrape site
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)

# 2. Create a list to hold the images and titles.
#hemisphere_image_urls = []
# Parse the resulting html with soup
#html = browser.html
#hemisphere_soup = soup(html, 'html.parser')
#hemisphere_image_urls = hemisphere_soup.find_all('a', class_ = ['itemLink', 'product-item'])

# 3. Write code to retrieve the image urls and titles for each hemisphere.
#for hemisphere_image_url in hemisphere_image_urls:
    #hemisphere = {}
    #img_url_rel = hemisphere_image_url['href']
    # Use the base url to create an absolute url
    #img_url = f'https://astrogeology.usgs.gov{img_url_rel}'
    #title = hemisphere_image_url.find('h3')
    #if title:
        #title.get_text()
        #print(img_url, title.get_text())
# This coding wasn't providing the four hemisphere images in a full jpg, which is why I didn't use it but it does provide a link
# to the image webpage.

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# Parse the data
html = browser.html
hemisphere_soup = soup(html, 'html.parser')
hemisphere_urls = hemisphere_soup.find_all('div', class_=['description'])
for hemisphere_url in hemisphere_urls:
    img_url_rel = hemisphere_url.a['href']
    img_url = f'https://astrogeology.usgs.gov{img_url_rel}' 
    
    browser.visit(img_url)
    
    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')
        
    hemispheres = {}
    img_url = img_soup.find('div', class_=['downloads']).a['href']
    title = img_soup.find('h2').get_text()
    hemispheres = {'img_url':img_url, 'title': title}
    hemisphere_image_urls.append(hemispheres)

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()
