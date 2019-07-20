# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 11:04:08 2018

@author: linzino
"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/zino/index.php")
def zino():
    return "Hello cheater!"

#新分頁
@app.route("/test/path")
def new_Path():
    return "Hello World /test/path!"


if __name__ == '__main__':
    app.run(debug=True)