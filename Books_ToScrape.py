#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Script used to test web_scraper():

from bs4 import BeautifulSoup as bs4
import requests
import pandas as pd

pages_to_scrape = int(input())
count = 0

def web_scraper(pages_to_scrape):
    pages = []
    prices = []
    stars = []
    titles = []
    urls = []

    for i in range(1, pages_to_scrape+1):
        url = ('http://books.toscrape.com/catalogue/page-{}.html').format(i)
        pages.append(url)

    for item in pages:
        page = requests.get(item)
        soup = bs4(page.text, 'html.parser')

    for i in soup.findAll('h3'):
        ttl = i.getText()
        titles.append(ttl)
    for j in soup.findAll('p', class_ = 'price_color'):
            price = j.getText()
            prices.append(price)
    for s in soup.findAll('p', class_ = 'star-rating'):
            for k,v in s.attrs.items():
                star = v[1]
                stars.append(star)
    divs = soup.findAll('div', class_='image_container')
    for thumbs in divs:
        tgs = thumbs.find('img',class_='thumbnail')
        url = 'http://books.toscrape.com/'+str(tgs['src'])
        complete_url = url.replace("../","")
        urls.append(complete_url)

    data = {'Title': titles, 'Prices': prices, 'Stars':stars, "URLs":urls}
    df = pd.DataFrame(data=data)
    df.index += 1
    df.to_excel("Books_ToScrape.xlsx")

web_scraper(pages_to_scrape)

