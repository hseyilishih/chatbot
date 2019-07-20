# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 01:00:17 2018

@author: linzino
"""


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('/qkB5Zg8hPmj1cqCTre2wmPAA5BYFLO84D5gNimCQrJcctCBs7rj/npScO0/I+V/3a1QaGASii2bM66epKO2coZ29wMHnBAyXqPGKkFpkrpHn2V+I/I4+sd4ZL5Jd5SBPqZtsWKaJwXaAfmxx3SNMwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('16ba3e7335ea47f5c3cfb3961de6e5af')

line_bot_api.push_message('U29bc9ff2f0e560d8fa2e85b78daa4ffa', TextSendMessage(text='Hello World!'))

@app.route("/callback", methods=['POST'])
def callback():

    
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
 

print('juhuhu')

if __name__ == '__main__':
    app.run(debug=True)

