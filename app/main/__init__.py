from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return "VulnTracker Ana Sayfa - Application Factory İskeleti Çalışıyor!"
