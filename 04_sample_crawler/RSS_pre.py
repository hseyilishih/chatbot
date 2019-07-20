# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 03:38:36 2018

@author: linzino
"""


# 練習 想爬體育版    https://udn.com/rssfeed/lists/2
# 

import feedparser
 
rss_url = 'https://udn.com/rssfeed/news/2/7227?ch=news'
 
# 抓取資料
rss = feedparser.parse(rss_url)

# 改為抓取標題
for i in rss['entries']:
    """ 撰寫程式"""