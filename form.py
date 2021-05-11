from flask_wtf import Form
from wtforms import StringField, SubmitField, validators, ValidationError, RadioField, DateField, SelectField
from model import UserRegister

class FormRegister(Form):
   """ 依照Model來建置相對應的Form  """
   username = StringField('姓名：', validators=[
       validators.DataRequired(),
       validators.Length(2, 10)
   ])
   phone = StringField('電話：', validators=[
       validators.DataRequired(),
       validators.Length(10),
   ])
   sex = RadioField('性別：', choices=[('male','男'),('female','女')])
   time = DateField('時間 (年/月/日)：', format='%Y/%m/%d')
   area = SelectField('地區：', choices=[('北','北部'),('中','中部'),('南','南部')])
   submit = SubmitField('完成')



   def validate_phone(self, field):
       if UserRegister.query.filter_by(phone=field.data).first():
           raise ValidationError('這支電話已報名過')

