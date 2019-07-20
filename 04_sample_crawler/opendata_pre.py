# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 03:17:35 2018

@author: linzino
"""

import requests #引入函式庫
import json
# data.taipei 一周天氣。
url = 'https://data.taipei/opendata/datalist/apiAccess?scope=resourceAquire&rid='

# RID
rid = 'e6831708-02b4-4ef8-98fa-4b4ce53459d9'

# 對網址請求資料
resp = requests.get(url+rid)
# 把回傳的資料轉換成json 格式方便我們抓取資料。
stopwater = json.loads(resp.text)

# 根據json 格式抓取第一筆資料
print(stopwater['result']['results'][0])


for result in stopwater['result']['results']:
""" 撰寫程式"""

