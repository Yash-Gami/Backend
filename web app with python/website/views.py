from flask import Blueprint, render_template,request,flash
from flask_login import login_required,current_user
from .models import User
from . import db

views = Blueprint('views', __name__)

@views.route('/',methods=['POST','GET'])
@login_required
def home():
    return render_template('module.html',user=current_user)
    



# @views.route("/",methods=['POST','GET'])
# @login_required
# def UserAuthentication(per):
#     print(per.split(","))
#     return render_template('module.html',user=current_user)












# def home():
#     if request.method == 'POST':
#         note = request.form.get('note')
#         if len(note) < 1:
#             flash('note is too short', category='error')
#         else:
#             new_note = Note(data=note, user_id=current_user.id)
#             db.session.add(new_note)
#             db.session.commit()
#             flash('note added', category='success')

#     return render_template('module.html',user=current_user)