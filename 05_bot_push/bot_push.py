# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 04:56:34 2018

@author: linzino
"""

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import feedparser

line_bot_api = LineBotApi('Channel Access Token')

userID = '使用者ID'



# function
def getNews():
    """
    建立一個抓最新消息的function
    """
    rss_url = 'https://udn.com/rssfeed/news/2/6638?ch=news'
    # 抓取資料
    rss = feedparser.parse(rss_url)
    # 抓取第一個文章標題
    title = rss['entries'][0]['title']
    # 抓取第一個文章標題
    link = rss.entries[0]['link']
    
    tmp = title + ' ' +link
    return tmp


# TextSendMessage
message = TextSendMessage(text='zino')
line_bot_api.push_message(userID, message )

# TextSendMessage
message =TextSendMessage( getNews())
line_bot_api.push_message(userID, message)

# 地理位置
message = LocationSendMessage(
            title='北車',
            address='hart',
            latitude=25.0477136,
            longitude=121.5167518
        )
line_bot_api.push_message(userID, message)

# 傳送貼圖
message = StickerSendMessage(
    package_id='1',
    sticker_id='10'
)
line_bot_api.push_message(userID, message)


# 詢問視窗
message = TemplateSendMessage(
    alt_text='你覺得這個機器人方便嗎？',
    template=ConfirmTemplate(
        text='你覺得這個課好嗎？',
        actions=[
            MessageTemplateAction(
                label='很棒！',
                text='ＧＯＯＤ5'
            ),
            MessageTemplateAction(
                label='有待加強',
                text='ＢＡＤ'
            )
        ]
    )
)
line_bot_api.push_message(userID, message)
 

# 選單介面
message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/DLN63CB.jpg',
                title='Menu',
                text='Please select',
                actions=[
                    MessageTemplateAction(
                        label='發生地點',
                        text='我要看發生地點'
                    ),
                    MessageTemplateAction(
                        label='文字雲週報',
                        text='我要看文字雲週報'
                    ),
                    URITemplateAction(
                        label='Uri',
                        uri='https://tw.appledaily.com/local/realtime/20180817/1412804'
                    )
                ]
            )
        )
line_bot_api.push_message(userID, message)


# 選單介面
message = TemplateSendMessage(
            alt_text='Buttons template',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/vkqbLnz.png',
                title='Menu',
                text='Please select',
                actions=[
                    MessageTemplateAction(
                        label='發生地點',
                        text='我要看發生地點'
                    ),
                    MessageTemplateAction(
                        label='文字雲週報',
                        text='我要看文字雲週報'
                    ),
                    URITemplateAction(
                        label='Uri',
                        uri='https://tw.appledaily.com/local/realtime/20180817/1412804'
                    )
                ]
            )
        )
line_bot_api.push_message(userID, message)

# 多選單
message = TemplateSendMessage(
    alt_text='Carousel template',
    template=CarouselTemplate(
        columns=[
            CarouselColumn(
                thumbnail_image_url='https://i.imgur.com/hzht3Nd.jpg',
                title='新聞預警',
                text='新聞來源-蘋果新聞',
                actions=[
                    MessageTemplateAction(
                        label='發生地點',
                        text='我要看發生地點'
                    ),
                    MessageTemplateAction(
                        label='文字雲週報',
                        text='我要看文字雲週報'
                    ),
                    URITemplateAction(
                        label='Uri',
                        uri='https://tw.appledaily.com/local/realtime/20180817/1412804'
                    )
                ]
            ),
            CarouselColumn(
                thumbnail_image_url='https://i.imgur.com/Dt97YFG.png',
                title='其他功能',
                text='這裡存放各種功能！',
                actions=[
                    MessageTemplateAction(
                        label='為機器人評分',
                        text='我想要評分'
                    ),
                    MessageTemplateAction(
                        label='更多新聞',
                        text='我要看報紙'
                    ),
                    MessageTemplateAction(
                        label='放鬆一下',
                        text='給我一個貼圖'
                    )
                ]
            )
        ]
    )
)
                
line_bot_api.push_message(userID, message)

# 圖片
message = ImageSendMessage(
    original_content_url='https://i.imgur.com/B9ftEHJ.jpg',
    preview_image_url='https://i.imgur.com/B9ftEHJ.jpg'
)
line_bot_api.push_message(userID, message)

# 多個圖片
 message = TemplateSendMessage(
            alt_text='ImageCarousel template',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/N3oQXjW.png',
                        action=PostbackTemplateAction(
                            label='postback1',
                            text='postback text1',
                            data='action=buy&itemid=1'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/OBdCHB9.png',
                        action=PostbackTemplateAction(
                            label='postback2',
                            text='postback text2',
                            data='action=buy&itemid=2'
                        )
                    )
                ]
            )
        )
line_bot_api.push_message(userID, message)