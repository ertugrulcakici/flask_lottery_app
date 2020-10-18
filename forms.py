from wtforms import Form,StringField,PasswordField,validators


#Login formu
class loginform(Form):
    username = StringField("Kullanıcı adı",validators=[validators.DataRequired("Burası dolu olmalıdır")])
    password = PasswordField("Şifre",validators=[validators.DataRequired("Burası dolu olmalıdır")])

#item formu
class itemform:
    item = StringField(label="Ekle",validators=[validators.DataRequired("Burası dolu olmalıdır")])
