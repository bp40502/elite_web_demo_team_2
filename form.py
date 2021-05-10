from flask_wtf import Form
from wtforms import StringField, SubmitField, validators, PasswordField, ValidationError, RadioField, DateTimeField
from wtforms.fields.html5 import EmailField

class FormRegister(Form):
   """ 依照Model來建置相對應的Form  """
   username = StringField('姓名', validators=[
       validators.DataRequired(),
       validators.Length(2, 10)
   ])
   phone = StringField('電話', validators=[
       validators.DataRequired(),
       validators.Length(10),
   ])
   sex = RadioField('性別', choices=[('value','男'),('value_two','女')])
   #time = DateTimeField()
   submit = SubmitField('完成')
