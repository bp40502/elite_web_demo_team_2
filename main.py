from flask import Flask, render_template
import os
from model import db, UserRegister
from flask_bootstrap import Bootstrap
from form import FormRegister

app = Flask(__name__, template_folder='wind')

pjdir = os.path.abspath(os.path.dirname(__file__))
#  新版本的部份預設為none，會有異常，再設置True即可。
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#  設置資料庫為sqlite3
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
   os.path.join(pjdir, 'data_register.sqlite')
app.config['SECRET_KEY'] = os.urandom(24)

db.init_app(app)
with app.app_context():
   db.create_all()

bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/story')
def story():
    return render_template('story.html')

@app.route('/rule')
def rule():
    return render_template('rule.html')

@app.route('/character')
def character():
    return render_template('character.html')

@app.route('/card')
def card():
    return render_template('card.html')

@app.route('/register', methods=['GET', 'POST'])
def register():   
   form = FormRegister()
   if form.validate_on_submit():
       user = UserRegister(
           username = form.username.data,
           phone = form.phone.data,
           sex = form.sex.data,
           time = form.time.data,
           area = form.area.data
       )
       db.session.add(user)
       db.session.commit()
       return '報名成功！'
   return render_template('register.html', form=form)

