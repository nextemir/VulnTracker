# pyrefly: ignore [missing-import]
from flask import Blueprint, render_template, request
from flask_login import login_required
from app import db
from app.models import Vulnerability
from sqlalchemy import select

# Blueprint nesnen (Oturum yapısına uygun 'bp')
bp = Blueprint('main', __name__)

@bp.route('/')
@bp.route('/index')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    # Modern SQLAlchemy 2.0 select sorgusu
    query = select(Vulnerability).order_by(Vulnerability.id.desc())
    # Sayfa başına 10 kayıt getirecek pagination motoru
    vulnerabilities = db.paginate(query, page=page, per_page=10, error_out=False)
    
    # Ajanın yazdığı o cyberpunk index.html dosyasını çağırıyoruz
    return render_template('main/index.html', vulnerabilities=vulnerabilities)