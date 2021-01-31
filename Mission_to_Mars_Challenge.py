#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[2]:


# Path to chromedriver
get_ipython().system('which chromedriver')


# In[3]:


# Set the executable path and initialize the chrome browser in splinter
from webdriver_manager.chrome import ChromeDriverManager
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[4]:


# Visit the mars nasa news site
url = 'https://mars.nasa.gov/news/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)


# In[5]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('ul.item_list li.slide')
#browser.quit()


# In[6]:


slide_elem.find("div", class_='content_title')


# In[7]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find("div", class_='content_title').get_text()
news_title


# In[8]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_="article_teaser_body").get_text()
news_p


# ### JPL Space Images Featured Image

# In[14]:


# Visit URL
url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url)


# In[16]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')#96425
full_image_elem.click()


# In[3]:


# Find the more info button and click that
#browser.is_element_present_by_text('More', wait_time=1)
#more_info_elem = browser.links.find_by_partial_text('More')
#more_info_elem.click()


# In[41]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[2]:


# find the relative image url
#img_url_rel = img_soup.select_one('figure.lede a img').get("src")
#img_url_rel


# In[1]:


# Use the base url to create an absolute url
#img_url = f'https://www.jpl.nasa.gov{img_url_rel}'
#img_url


# ### Mars Facts

# In[15]:


df = pd.read_html('http://space-facts.com/mars/')[0]

df.head()


# In[16]:


df.columns=['Description', 'Mars']
df.set_index('Description', inplace=True)
df


# In[17]:


df.to_html()


# ### Mars Weather

# In[11]:


# Visit the weather website
url = 'https://mars.nasa.gov/insight/weather/'
browser.visit(url)


# In[12]:


# Parse the data
html = browser.html
weather_soup = soup(html, 'html.parser')


# In[13]:


# Scrape the Daily Weather Report table
weather_table = weather_soup.find('table', class_='mb_table')
print(weather_table.prettify())


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[165]:


# 1. Use browser to visit the URL 
url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
browser.visit(url)


# In[18]:


html = browser.html
html_soup = soup(html, 'html.parser')


# In[24]:


titles = html_soup.find('h3')


# In[29]:


for title in titles:
    title = html_soup.find('h3').text
    print(title)


# In[37]:


divs = browser.find_by_tag("div")
divs


# In[164]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []
#variable link by filtering

# 3. Write code to retrieve the image urls and titles for each hemisphere.
#for image in  :

#image = browser.find_all('div', class_="description")
#links = browser.find_by_css("div.downloads a")
web_links = browser.find_by_css("div.item a")

for i in range(len(web_links)):
    web_link = web_links[i]["href"]
    browser.click_link_by_href(web_link)
    #browser.links.find_by_href(web_link)
    img_links = browser.find_by_css("div.downloads a")
    for idx in range(len(img_links)):
        print(img_links[idx]["href"]) 
    browser.back()
#for link in links:
    #print(links)

#print(len(links))     
#browser.find_by_links('full_image')
#for idx in range(len(links)):
    #print(links[idx]["href"])


# In[172]:


hemisphere_image_urls = []

links = browser.find_by_css("a.product-item h3")
for i in range(len(links)):
    hemisphere = {}
    browser.find_by_css("a.product-item h3")[i].click()
    sample_elem = browser.links.find_by_text('Sample')[0]
    hemisphere['img_url'] = sample_elem['href']
    hemisphere['title'] = browser.find_by_css("h2.title").text
    hemisphere_image_urls.append(hemisphere)

    browser.back()


# In[170]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[80]:


# 5. Quit the browser
browser.quit()


# In[ ]:




