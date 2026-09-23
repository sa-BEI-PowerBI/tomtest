# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 14:09:57 2026

@author: E153152
"""

from flask import Flask
application = Flask(__name__) # AWS looks for 'application' by default

@application.route('/')
def hello_world():
    return "Hello from AWS hosted via Git and Python!"

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000)