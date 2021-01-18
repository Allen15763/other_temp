# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 11:27:51 2021

@author: allenli
"""
# hybris_checking
# issues: more than 3 tables, random table content
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

productname = []
productprice = []
stockno = []
stock_url = []
promo_url = []
description = []
description2 = []
description3 = []
promo = []
h4p = []

fail1 = []
fail2 = []

for p in range(3):
    time.sleep(random.uniform(5, 7))
    try:
        # request_url = f"https://www.watsons.com.tw/%E8%87%89%E9%83%A8%E4%BF%9D%E9%A4%8A/c/1041?q=:igcBestSeller&page={p}&resultsForPage=32&text=&sort=igcBestSeller&deliveryType="
        # request_url = f'https://www.watsons.com.tw/%E5%8C%96%E5%A6%9D%E5%93%81%E9%A6%99%E6%B0%B4/c/1044?q=:igcBestSeller&page={p}&resultsForPage=32&text=&sort=igcBestSeller&deliveryType='
        # request_url = f'https://www.watsons.com.tw/%E9%86%AB%E7%BE%8E/c/1043?q=:igcBestSeller&page={p}&resultsForPage=32&text=&sort=igcBestSeller&deliveryType='
        # request_url = f'https://www.watsons.com.tw/%E4%BF%9D%E5%81%A5/c/1049?q=:igcBestSeller&page={p}&resultsForPage=32&text=&sort=igcBestSeller&deliveryType='
        # request_url = f'https://www.watsons.com.tw/%E7%BE%8E%E9%AB%94%E7%BE%8E%E9%AB%AE/c/1048?q=:igcBestSeller&page={p}&resultsForPage=32&text=&sort=igcBestSeller&deliveryType='
        request_url = f'https://www.watsons.com.tw/%E6%97%A5%E7%94%A8%E5%93%81/c/1045?q=:igcBestSeller&page={p}&resultsForPage=32&text=&sort=igcBestSeller&deliveryType='
        # request_url = f'https://www.watsons.com.tw/%E7%94%B7%E6%80%A7%E7%94%A8%E5%93%81/c/1042?q=:igcBestSeller&page={p}&resultsForPage=32&text=&sort=igcBestSeller&deliveryType='
        # request_url = f'https://www.watsons.com.tw/%E9%81%8B%E5%8B%95%E4%BC%91%E9%96%92/c/1051?q=:igcBestSeller&page={p}&resultsForPage=32&text=&sort=igcBestSeller&deliveryType=' # 運動
        # request_url = f
        response = requests.get(request_url)
        response_text = response.text
        soup =BeautifulSoup(response_text, "html.parser")
        
        # productname = [e.text.replace('\xa0', '-').replace('\n', '').replace('\t', '') for e in soup.select(".gtmAlink .h1")]
        for e in soup.select(".gtmAlink .h1"):
            productname.append(e.text.replace('\xa0', '-').replace('\n', '').replace('\t', ''))
        
        # productprice = [e.text for e in soup.select(".productNameInfo .h2")]
        for e in soup.select(".productNameInfo .h2"):
            productprice.append(e.text)
    
        item = soup.find_all('div', class_='productItemPhotoContainer')
        for e in item:
            stockno.append(e.find('a').get('href')[-9:])
              
        for e in item:
            stock_url.append("https://www.watsons.com.tw" + e.find('a').get('href'))
            
    except:
        print("You're blocked: " + p)
        # fail1.append(p)
        break

for e, sku in zip(stock_url, stockno):
    promo_url.append(e + "/showAction?isQuickView=false&codeVarSel=" + sku)        

        
for stock in stock_url:
    try:
        request_stock_url = stock
        # time.sleep(random.uniform(3, 5))
        response_stock = requests.get(request_stock_url)
        soup_stock = BeautifulSoup(response_stock.text, "html.parser")
        try:            
            td = soup_stock.find_all('table')[0]
            description.append(td.text)
        except:
            description.append('none')
            pass
        try:
            td2 = soup_stock.find_all('table')[1]            
            description2.append(td2.text)
        except:
            description2.append('none')
            pass                
        try:
            ori = soup_stock.select('h4+ p')[0]
            if len(str(ori.text)) > 5:
                ori = soup_stock.select('h4+ p')[1]
                h4p.append(ori.text)
            else:
                h4p.append(soup_stock.select('h4+ p')[0].text)
        except:
            h4p.append('none')
            pass                
        try:            
            td3 = soup_stock.find_all('table')[2]                
            description3.append(td3.text) 
        except:
            description3.append('none')
            continue
    except:
        print("failed to access: " + stock)
        fail1.append(stock)
        break

    
for promotion in promo_url:
    try:
        # time.sleep(random.uniform(1, 3))
        response_pro = requests.get(promotion)
        response_prosoup = BeautifulSoup(response_pro.text, "html.parser")
        try:
            pro = response_prosoup.select('.drop-box span')
            re = [x.text.replace('<span>', '').replace('</span>', '') for x in pro ]
            promo.append(re)
        except:
            promo.append('none')
            continue                           
    except:
        print("failed to access: " + promotion)
        fail2.append(promotion)
        break

df = pd.DataFrame()
df["name"] = productname
df["price"] = productprice
df["stockno"] = stockno

df2 = pd.DataFrame()
df2["name"] = productname
df2["price"] = productprice
df2["stockno"] = stockno
df2["規格"] = description
df2["屬性"] = description2
df2["廠商"] = description3
df2["promo"] = promo
df2["產地"] = pd.Series(h4p)
print(df2)
df3 = pd.DataFrame()
df3["failed log_detail"] = fail1
df3["failed log_pro"] = fail2

writer = pd.ExcelWriter('products.xlsx')
df.to_excel(writer, sheet_name="df1")
df2.to_excel(writer, sheet_name="df2")
df3.to_excel(writer, sheet_name="df3")
writer.save()
writer.close()

# brand = []
# specification = []
# Origin = []
# size = []
# weight = []
# environment = []
# pickup = []
        # if td.find_all('td', 'td2')[0].text not in description:
        #     description.append(td.find_all('td', 'td2')[0].text)
        # if td.find_all('td', 'td2')[1].text not in brand:
        #     brand.append(td.find_all('td', 'td2')[1].text)
        # if td.find_all('td', 'td2')[2].text not in specification:
        #     specification.append(td.find_all('td', 'td2')[2].text)
        # if td.find_all('td', 'td2')[3].text not in Origin:
        #     Origin.append(td.find_all('td', 'td2')[3].text)
        # if td.find_all('td', 'td2')[4].text not in size:
        #     size.append(td.find_all('td', 'td2')[4].text)
        # if td.find_all('td', 'td2')[5].text not in weight:
        #     weight.append(td.find_all('td', 'td2')[5].text)
        # if td.find_all('td', 'td2')[6].text not in environment:
        #     environment.append(td.find_all('td', 'td2')[6].text)
        # if td.find_all('td', 'td2')[7].text not in pickup:
        #     pickup.append(td.find_all('td', 'td2')[7].text)
# df2["brand", "specification", "Origin", "size", "weight", "environment", "pickup"] = brand, specification, Origin, size, weight, environment, pickup