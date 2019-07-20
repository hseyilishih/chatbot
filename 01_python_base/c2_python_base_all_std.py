#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 13:06:38 2018

@author: zino
"""

#--------頁籤-------- 


# 給予值
anyname = "It's str."
# 直接執行 變數名稱  代表請程式 把變數內資料輸出
anyname

num_var = 1
num_var

float_var = 0.5
float_var


# 運算
a = 3
b = 2

c = a ** b
c

# 字串相加
g = anyname+str(c)



# 變數覆蓋

var = 10
var

var = '被覆蓋掉了'
var


# List

a = [1,2,3,4,5]
a
print(a)

# 取出List資料
a[4]

# 計算長度
print(len(a))

# 常見操做
a.append(7)
a.append(9)
a.append(5)
a.sort()


# Dictionary

dic = {'key1':'Value1',
       'key2':'Value2',
       'key3':'Value3'}

# 取出Dictionary資料
dic['key2']


# if 判斷式
# python 是以縮排
a= 50 
if a >10:
    print('a大於10')
else:
    print('a不大於10')
    
# 練習    

var = '今日頭條新聞，公司開設預警機器人專班'

'TMR' in var

    
    

# for 迴圈 思維

print(1)
print(2)
print(3)
print(4)
print(5)

for i in [1,2,3,4,5]:
    print(i)


## 題目使用for 迴圈列出以下字串：
str_list = ['在與公平會和解後，',
            '美國高通明年第567667',
            '「台灣營運與製造工程暨測試中心（COMET）」',
            '營運資深副總裁陳若文負責']

# 在此寫解答



## 如果有多的如何放入str_list
extr_list = ['「京都動畫縱火案」增至34死',
            '開山里關我什麼事']
# 在此寫解答




# Function
    
def str_Mi(a,b):
    return a+b

str_Mi(1,2)

g=str_Mi(1,2)



# 引用 套件 datetime
from datetime import datetime
# 現在時間
datetime.now()


# 組合技能 
# 陣列＋字典 整理資料

contents = [{'date':'2017.8.17',
             'title':'南投地震 規模4.1',
             'link':'http://example1.com'},
           {'date':'2017.8.17',
            'title':'律師團-續奮戰 直到全獲償',
            'link':'http://example1.com'}]


# 練習抓出title資料
contents[0]['title']


# 整理資料

news = []



import pandas as pd 

df = pd.DataFrame(news)
df.to_excel('dff.xls')


