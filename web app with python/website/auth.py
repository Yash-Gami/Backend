from flask import Blueprint,render_template,request,flash,redirect,url_for
from . import db,sendMail
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,login_required,logout_user,current_user
from . import views

auth = Blueprint('auth',__name__)



# mail = Mail(app)


@auth.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()    
        per = user.permission.split(",")
        name = user.first_name
    
        if user:
            if check_password_hash(user.password, password):
                otpverify = sendMail(email,name)

                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                # return redirect(url_for("views.yash()",per=user.permission))
                # return redirect(url_for('views.home'))
                return render_template('module.html',user=current_user,per=per)
            else:
                flash('incorrect password, try again', category='error')
        else:
            flash('Email does not exit',category = 'error')
    return render_template('index.html',user=current_user)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/signup", methods=['GET','POST'])
@login_required
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        permission = request.form.get('permission')
        if permission[-1] != ',':
            permission = str(permission) + ','

    



        user = User.query.filter_by(email=email).first()

        if user:
            flash('email already exists', category='error')
        elif len(email) < 4:
            flash('email should be greater than 4 character',category='error')
        elif len(first_name) < 2:
            flash('first name should be greater than 2 character',category='error')
        elif password1 != password2:
            flash('password don\'t match',category='error')
        elif len(password1) < 7:
            flash('password should be greater than 7 character',category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'), permission=permission)
            db.session.add(new_user)
            db.session.commit()
            # login_user(user, remember=True)
            flash('user created',category='sucess')
            # return redirect(url_for('views.home'))
            return redirect(url_for('auth.login'))
    return render_template('signup2.html',user=current_user)
