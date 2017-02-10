#/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

from itsdangerous import URLSafeTimedSerializer
from .. import app

ts =  URLSafeTimedSerializer(app.config["SECRET_KEY"])