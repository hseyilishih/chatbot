# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 03:17:35 2018

@author: linzino
"""

import requests #引入函式庫
import json
# data.taipei 停水資訊api連結。
url = 'http://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid='

# RID
rid = 'a242ee9b-b954-4ae9-9827-2344c5dfeaea'

# 對網址請求資料
resp = requests.get(url+rid)
# 把回傳的資料轉換成json 格式方便我們抓取資料。
stopwater = json.loads(resp.text)
# 根據json 格式抓取第一筆資料
print(stopwater['result']['results'][2]['Description'])

# 整理所有資料
rows = []

for result in stopwater['result']['results']:
    tmp =  {'_id': result['_id'],
    'SW_No': result['SW_No'],
    'FS_Date': result['FS_Date'],
    'FC_Date': result['FC_Date'],
    'SW_Area': result['SW_Area'],
    'Description': result['Description'],
    'PubDate': result['PubDate']}
    rows.append(tmp)


import pandas as pd
df = pd.DataFrame(rows)
df.to_excel('water.xls')

