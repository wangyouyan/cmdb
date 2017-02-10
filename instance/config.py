#/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask

DEBUG = True
dbhost = '127.0.0.1:3306'
dbuser = 'lenovo'
dbpass = 'abcd-1234'
dbname = 'assets'

DB_URI = 'mysql://' + dbuser + ':' + dbpass + '@' + dbhost + '/' + dbname

app = Flask(__name__)
