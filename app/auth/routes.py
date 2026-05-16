from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user
from app.auth import bp
from app.auth.forms import RegisterForm, LoginForm
from app.models import User
from app import db

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.execute(db.select(User).filter_by(username=form.username.data)).scalar()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            flash("Başarıyla giriş yaptınız.", "success")
            return redirect(url_for('main.index'))
        else:
            flash("Geçersiz kullanıcı adı veya şifre.", "danger")
    return render_template('auth/login.html', form=form)

@bp.route('/logout')
def logout():
    logout_user()
    flash("Oturum başarıyla kapatıldı.", "info")
    return redirect(url_for('auth.login'))

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
