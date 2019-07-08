#!/bin/env python3
# coding:utf-8

"""
# Author:   Harvey.Wang
# Data:     
# Desc:     
"""

from app import app
from flask import render_template, g

@app.route('/template')
def template():
    render_template('template.html', **locals())

@app.route('/')
@app.route('/index')
def index():
    page_settings = g.page_settings['index']
    return render_template('index.html', **locals())


@app.route('/aboutme')
def aboutme():
    page_settings = g.page_settings['aboutme']
    return render_template('aboutme.html', **locals())


@app.route('/blog')
def blog():
    pass


@app.route('/blog/<filename>')
def showBlog(filename):
    pass


@app.route('/contactme')
def contactme():
    pass


@app.before_request
def before_request():
    g.page_settings = app.config['PAGE_SETTINGS']
