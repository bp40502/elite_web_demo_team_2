from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class UserRegister(db.Model):
   """記錄使用者資料的資料表"""
   __tablename__ = 'UserRegister'
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(50), unique=False, nullable=False)
   phone = db.Column(db.String(15), unique=True, nullable=False)
   sex = db.Column(db.String(10), nullable=False)
   time = db.Column(db.String(30), nullable=False)
   area = db.Column(db.String(10), nullable=False)

   def __repr__(self):
       return 'username:%s, email:%s' % (self.username, self.phone)
