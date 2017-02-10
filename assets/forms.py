#/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

from flask_wtf import Form
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired,Email

from .util.validators import Unique
from .models import User

class EmailPasswordFrom(Form):
    email = StringField('Email',validators=[DataRequired(),Email],Unique(User,User.email,message='该邮箱已经注册'))
    password = PasswordField('Password',validators=[DataRequired()])
