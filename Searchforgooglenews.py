# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 13:23:32 2020

@author: allenli
"""

import requests
from bs4 import BeautifulSoup

def get_data(search):
    result_text_cs = '.VDXfz'
    # 1st request and parse: movie_url

    query_string_parameters = {
        'q': search,
        'hl': 'zh-TW',
        'gl': 'TW',
        'ceid': 'TW:zh-Hant'
    }
    request_url = 'https://news.google.com/search'
    response = requests.get(request_url, params=query_string_parameters, verify = False)
    soup = BeautifulSoup(response.text, "html.parser")     
    
    #to get results title
    title = soup.find_all('div', class_='xrnccd') # 找div 後面區塊是__的
    titles = [t.find('span').text for t in title] # 在該div區塊取出span的class後面內容
    print(titles)
    
    #to get results url
    result_text_hrefs = [e.get('href') for e in soup.select(result_text_cs)] 
    print(result_text_hrefs)

print(get_data("covid"))



 