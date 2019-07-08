#!/bin/env python3
# coding:utf-8

"""
# Author:   Harvey.Wang
# Data:     
# Desc:     
"""

import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

PAGE_SETTINGS = {
    "index": {
        "menu": [
            {"tag": "#section1", "name": "Blog"},
            {"tag": "#section2", "name": "About Me"},
            {"tag": "#section3", "name": "My Work"},
            {"tag": "#section4", "name": "Contact Me"}
        ],
        "title": "Index Page"
    },
    "aboutme": {
        "title": "About Me"
    },
    "mywork": {
        "title": "My Work"
    },
    "contactme": {
        "title": "Contact Me"
    }
}

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASEDIR, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(BASEDIR, 'migration')
