#!python3
# -*- coding: utf-8 -*-
from pathlib import Path
from flask import Flask, render_template, Markup, request, jsonify
import logging.config
app = Flask(__name__)

@app.route("/")
def hello():
    name ="ME!"
    items = ["aa", "bb", "ccc"]
    common = {"siteTitle":"sample flask website"}
    return render_template("views/index.html", name=name, items=items, common=common)

@app.route('/user/<username>')
def show_user_name(username):
    name ="inputed user name is...." + username
    return render_template("views/index.html", name=name)

@app.route('/plus/<int:numb>')
def calcPlus(numb):
    numb = numb + 4
    name = "plus result:" + str(numb)
    return render_template("views/index.html", name=name)

@app.route('/markupSample')
def markupSample():
    #Markup return webelement object. but replaced Parameter String has markup, then escape simply str.
    return Markup('<strong>Hello {}!</strong>').format('<blink>hacker</blink>')

if __name__ == '__main__':
    #using log.conf for develop mode.
    logging.config.fileConfig(fname='env/log_develop.conf', disable_existing_loggers=False)
    app.run(host='0.0.0.0', debug=True, port=5002)
else:
    #using log.conf for deploy mode.
    logging.config.fileConfig(fname='env/log_honban.conf', disable_existing_loggers=False)
