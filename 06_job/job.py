# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 03:52:43 2018

@author: linzino
"""

import schedule
import time

def job():
    print("I'm working...")

schedule.every(5).seconds.do(job)
schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
    

# 列出工作目錄
schedule.jobs

# 列出工作目錄
schedule.clear()
schedule.jobs


# 針對特定工作
second_5_j = schedule.every(5).seconds.do(job)
schedule.jobs
schedule.cancel_job(second_5_j)
