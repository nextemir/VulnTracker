from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from app.models import User

class LoginForm(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[
        DataRequired(message="Lütfen kullanıcı adınızı girin.")
    ])
    password = PasswordField('Şifre', validators=[
        DataRequired(message="Lütfen şifrenizi girin.")
    ])
    remember = BooleanField('Beni Hatırla')
    submit = SubmitField('Giriş Yap')

class RegisterForm(FlaskForm):
    username = StringField('Kullanıcı Adı', validators=[
        DataRequired(message="Lütfen bir kullanıcı adı girin."),
        Length(min=3, max=64, message="Kullanıcı adı 3 ile 64 karakter arasında olmalıdır.")
    ])
    email = StringField('E-posta', validators=[
        DataRequired(message="Lütfen bir e-posta adresi girin."),
        Email(message="Geçerli bir e-posta adresi girin.")
    ])
    password = PasswordField('Şifre', validators=[
        DataRequired(message="Lütfen şifrenizi girin."),
        Length(min=6, message="Şifreniz en az 6 karakter olmalıdır.")
    ])
    confirm_password = PasswordField('Şifre (Tekrar)', validators=[
        DataRequired(message="Lütfen şifrenizi tekrar girin."),
        EqualTo('password', message="Şifreler eşleşmiyor.")
    ])
    submit = SubmitField('Kayıt Ol')

    def validate_username(self, field):
        from app import db
        user = db.session.execute(db.select(User).filter_by(username=field.data)).scalar()
        if user:
            raise ValidationError("Bu kullanıcı adı zaten alınmış. Lütfen başka bir tane seçin.")

    def validate_email(self, field):
        from app import db
        user = db.session.execute(db.select(User).filter_by(email=field.data)).scalar()
        if user:
            raise ValidationError("Bu e-posta adresi zaten kullanımda.")
