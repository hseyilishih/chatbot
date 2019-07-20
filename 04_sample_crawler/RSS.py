# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 03:38:36 2018

@author: linzino
"""

import feedparser
 
rss_url = 'https://udn.com/rssfeed/news/2/6638?ch=news'
 
# 抓取資料
rss = feedparser.parse(rss_url)
 
# 抓取rss來源標題
print(rss['feed']['title'])

# 查看文章数量
print(len(rss['entries']))

# 抓取第一個文章標題
print(rss['entries'][1]['title'])

# 抓取第一個文章標題
print(rss.entries[1]['link'])

# 抓取第一個文章摘要
print(rss.entries[1]['summary'])

for i in rss['entries']:
    print(i['summary'])