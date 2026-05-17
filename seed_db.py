from app import create_app, db
from app.models import User, Vulnerability, UserRole
from sqlalchemy import select

app = create_app()

with app.app_context():
    # Check if admin exists
    admin = db.session.scalar(select(User).filter_by(username="admin"))
    if not admin:
        admin = User(username="admin", email="admin@cybergate.local", role=UserRole.ADMIN)
        admin.set_password("CyberGate2026!")
        db.session.add(admin)
        db.session.commit()
        print("Admin user created.")
    else:
        print("Admin user already exists.")

    # Create 12 vulnerabilities
    existing_count = db.session.query(Vulnerability).filter_by(user_id=admin.id).count()
    if existing_count < 12:
        for i in range(1, 13):
            vuln = Vulnerability(
                title=f"SQL Injection Test {i}" if i % 2 == 0 else f"XSS Vulnerability {i}",
                description=f"Auto-generated test description {i} for pagination.",
                severity="Critical" if i % 4 == 0 else "Medium",
                user_id=admin.id
            )
            db.session.add(vuln)
        db.session.commit()
        print(f"12 vulnerabilities injected successfully.")
    else:
        print("Vulnerabilities already injected.")
