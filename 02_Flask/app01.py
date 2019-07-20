# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 11:04:08 2018

@author: linzino
"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

if __name__ == '__main__':
    app.run(debug=True)