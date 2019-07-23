#!/bin/env python3
# coding:utf-8

"""
# Author:   Harvey.Wang
# Data:     
# Desc:     
"""

from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

app = Flask('__name__')
app.config.from_object('app.config')
# db = SQLAlchemy(app)


from routes import views