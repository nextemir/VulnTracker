# app/main/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class VulnerabilityForm(FlaskForm):
    title = StringField('Zafiyet Başlığı', validators=[
        DataRequired(message="Zafiyet başlığı boş bırakılamaz."),
        Length(min=5, max=100, message="Başlık en az 5, en fazla 100 karakter olmalıdır.")
    ])
    
    description = TextAreaField('Detaylı Açıklama / PoC Adımları', validators=[
        DataRequired(message="Zafiyet açıklaması boş bırakılamaz.")
    ])
    
    severity = SelectField('Kritiklik Derecesi', choices=[
        ('KRİTİK', 'Kritik (Critical)'),
        ('YÜKSEK', 'Yüksek (High)'),
        ('ORTA', 'Orta (Medium)'),
        ('DÜŞÜK', 'Düşük (Low)')
    ], validators=[DataRequired(message="Lütfen bir kritiklik derecesi seçiniz.")])
    
    submit = SubmitField('Zafiyeti Sisteme İşle')
