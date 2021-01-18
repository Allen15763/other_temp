# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 10:54:13 2020

@author: allenli
"""

from selenium import webdriver
import time
import random
import pandas as pd

item_page = []
for p in range(1, 10600):
    items_xpath ="//li[@class='column-grid-container__column'][{}]//div[@class='sc-AykKC cVdLkC']".format(p)
    item_page.append(items_xpath)

        
content_name = "//tr[2]/td[2]//p"
content_country = "//tr[5]/td[2]//p"
content_price = "//div[@class='salepage-price cms-moneyColor']"
content_company = "//tr[12]/td[2]//p"

driver_path = "C:/Users/allenli/OneDrive - A.S. Watson Group/Desktop/coding/chromedriver.exe"
cosmed_home = "https://shop.cosmed.com.tw/v2/official/SalePageCategory/216486?sortMode=Sales"
driver = webdriver.Chrome(executable_path=driver_path) # Use Chrome
driver.get(cosmed_home)


db = []
for c in item_page:
    columns = []
    values = []
    #window_before = driver.window_handles[0]
    
    #rolling="var action=document.documentElement.scrollTop=10000"
    #driver.execute_script(rolling)
    
    time.sleep(random.uniform(5, 7))
    try:
        x = driver.find_element_by_xpath(c)
        x.click()
    except:
        pass #略過 ❮本次❯ 迴圈，繼續進入下去等於後面值空白一列
    time.sleep(random.uniform(6, 8))
    #window_after = driver.window_handles[1]
    #driver.switch_to_window(window_after)
    try:
        t = driver.find_element_by_xpath(content_name).text
    except:
        t = ''        
    try:
        p = driver.find_element_by_xpath(content_price).text
    except:
        p = ''
    try:
        co = driver.find_element_by_xpath(content_company).text
    except:
        co = ''
    try:
        cou =driver.find_element_by_xpath(content_country).text
    except:
        cou = ''
    print("Name:" + t, "Price:" + p, "Pro:" + co)

    columns += ['title', 'price', 'company', 'country']
    values += [t, p, co, cou]
    ndb = pd.DataFrame(data=values, index=columns).T
    db.append(ndb)
#    db = {
#      "商品名:" : t.text,
#      "價格:" : p.text,
#      "製造商:" : co.text
#      }
#    print(db)
    driver.back()
    if c / 40 % 0
    time.sleep(random.uniform(2, 3))
#print(driver.current_url)



print(db)

driver.close()
db = pd.concat(db, ignore_index=True)
db.info()
db.to_excel('./cosmed.xlsx')