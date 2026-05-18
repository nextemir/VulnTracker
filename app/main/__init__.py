# pyrefly: ignore [missing-import]
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import Vulnerability
from sqlalchemy import select
from app.main.forms import VulnerabilityForm
from datetime import datetime, timezone, timedelta

# Türkiye Saat Dilimi: UTC+3 (Kalıcı yaz saati)
TR_TZ = timezone(timedelta(hours=3))

# Blueprint nesnen (Oturum yapısına uygun 'bp')
bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    # Modern SQLAlchemy 2.0 select sorgusu (sadece açık olanları listele)
    query = select(Vulnerability).where(Vulnerability.is_resolved == False).order_by(Vulnerability.id.desc())
    # Sayfa başına 10 kayıt getirecek pagination motoru
    vulnerabilities = db.paginate(query, page=page, per_page=10, error_out=False)
    
    # Ajanın yazdığı o cyberpunk index.html dosyasını çağırıyoruz
    return render_template('main/index.html', vulnerabilities=vulnerabilities)

@bp.route('/vulnerability/add', methods=['GET', 'POST'])
@login_required
def add_vulnerability():
    form = VulnerabilityForm()
    if form.validate_on_submit():
        vulnerability = Vulnerability(
            title=form.title.data,
            description=form.description.data,
            severity=form.severity.data,
            user=current_user,
            created_at=datetime.now(TR_TZ)  # UTC+3 Türkiye Zaman Damgası
        )
        db.session.add(vulnerability)
        try:
            db.session.commit()
            flash('Yeni zafiyet sisteme başarıyla işlendi.', 'success')
            return redirect(url_for('main.index'))
        except Exception as e:
            db.session.rollback()
            flash('Sistemsel bir hata oluştu, işlem güvenli bir şekilde geri alındı.', 'danger')
            # Gerçek kurumsal senaryoda burada loglama yapılır (örn: current_app.logger.error(e))
    
    return render_template('main/vulnerability_form.html', title='Yeni Zafiyet Ekle', form=form)

@bp.route('/vulnerability/<int:vuln_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_vulnerability(vuln_id):
    vulnerability = db.get_or_404(Vulnerability, vuln_id)
    form = VulnerabilityForm()
    
    if form.validate_on_submit():
        vulnerability.title = form.title.data
        vulnerability.description = form.description.data
        vulnerability.severity = form.severity.data
        vulnerability.is_resolved = form.is_resolved.data
        try:
            db.session.commit()
            flash('Zafiyet kaydı başarıyla güncellendi.', 'success')
            return redirect(url_for('main.index'))
        except Exception as e:
            db.session.rollback()
            flash('Sistemsel bir hata oluştu, güncelleme işlemi geri alındı.', 'danger')
    elif request.method == 'GET':
        form.title.data = vulnerability.title
        form.description.data = vulnerability.description
        form.severity.data = vulnerability.severity
        form.is_resolved.data = vulnerability.is_resolved
        
    return render_template('main/vulnerability_form.html', title='Zafiyeti Düzenle', form=form, vulnerability=vulnerability)

@bp.route('/vulnerability/<int:vuln_id>/delete', methods=['POST'])
@login_required
def delete_vulnerability(vuln_id):
    vulnerability = db.get_or_404(Vulnerability, vuln_id)
    db.session.delete(vulnerability)
    try:
        db.session.commit()
        flash('Zafiyet kaydı sistemden kalıcı olarak silindi.', 'info')
    except Exception as e:
        db.session.rollback()
        flash('Silme işlemi sırasında hata oluştu, işlem durduruldu.', 'danger')
    return redirect(url_for('main.index'))
