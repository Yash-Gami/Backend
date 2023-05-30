from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
from flask_mail import Mail,Message
from flask import render_template
from random import randint




db = SQLAlchemy()
DB_NAME = "main.db"


def create_app():
    app = Flask(__name__,template_folder='template')
    app.config['SECRET_KEY'] = 'hasdhkashdkasdhas'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    app.config["MAIL_SERVER"]="smtp.gmail.com"
    app.config["MAIL_PORT"] = "587"
    app.config["MAIL_USERNAME"] = "yashflask@gmail.com"
    app.config["MAIL_PASSWORD"] = "lmzmzrcorgbmeuxb"
    app.config["MAIL_USE_TLS"] = True
    app.config["MAIL_USE_SSL"] = False
    db.init_app(app)
    global mail
    mail = Mail(app)    


    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')


    from .models import User, Note

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))


    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print("Created Databse!")



def sendMail(email,name):
    
    if email != "admin@gmail.com":
        otp = randint(100000, 999999)
        msg = Message('E-mail Verification',sender='yashflask@gmail.com',recipients=[email])
        # msg.body = ("Hello "+<b>name</b>+"your E-mail has been verified for the login \nBelow is the OTP for login valid for next 5 min")
        msg.html = render_template('email.html',name=name,otp=otp)
        mail.send(msg)
        return otp
    else:
        print("Mail not sent")