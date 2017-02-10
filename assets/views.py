#/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:Rain Wang
#E-mail:wyyservice@gmail.com

from flask import render_template,redirect,url_for,Flask
from . import app,db
from .forms import EmailPasswordFrom
from .util import ts,send_email

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home<h1>'

@app.route('/login',methods=['GET','POST'])
def login():
    form = EmailPasswordFrom()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('login.html',form=form)

@app.route('/accounts/create',methods=["GET","POST"])
def create_account():
    form = EmailPasswordFrom()
    if form.validate_on_submit():
        user = User(
            email = form.email.data,
            password = form.password.data
        )
        db.session.add(user)
        db.session.commit()

    #Now we'll send the email confirmation link
        subject = "Confirm your email"
        token = ts.dump(self.email,salt='email-confirm-key')
        confirm_url = url_for(
            'confirm_email',
            token=token,
            _external=True)

        html = render_template(
            'email/activate.html'
            confirm_url=confirm_url)

        #假设assets/util/下定义了send_mail
        send_email(user.email,subject,html)
        return redirect(url_for("index"))
    return render_template("accounts/create.html",form=form)

@app.route('/confirm/<token>')
def confirm_email(token):
    try:
        email = ts.loads(token,salt="email-confirm-key", max_age=86400)
    except:
        abort(404)

    user = User.query.filter_by(email=email).first_or_404()
    user.email_confirmed = True

    db.session.add(user)
    db.session.commit()
    return redirect(url_for('Sign In'))

if __name__=='__main__':
    app.debug = True
    app.run()