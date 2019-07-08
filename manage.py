#!/bin/env python3
# coding:utf-8

"""
# Author:   Harvey.Wang
# Data:     
# Desc:     
"""

from app import app

if __name__ == '__main__':
    app.debug = True
    # app.run(host='127.0.0.1', port=5002)
    app.run()
