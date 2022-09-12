from random import random
from flask import Flask
import math

APPX = Flask(__name__)

@APPX.route('/users')
def user_names():
    ul = ["john","alic","lucy","aria","hexa"]
    return ul[(random() * 100) % len(ul)]

@APPX.route('/apps')
def app_names():
    al = ["twitter","facebook","google","instagram","snapchat"]
    return al[(random() * 100) % len(al)]

if __name__ == '__main__':
    APPX.run(host='0.0.0.0', port=8081, debug=True)
