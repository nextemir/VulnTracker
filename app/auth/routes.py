from flask import render_template, redirect, url_for, flash
from app.auth import bp
from app.auth.forms import RegisterForm
from app.models import User
from app import db

@bp.route('/login')
def login():
    return "Giriş Sayfası (Yapım Aşamasında)"

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Kayıt başarılı! Lütfen giriş yapın.", "success")
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)
