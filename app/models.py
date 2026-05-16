from typing import Optional, List
from datetime import datetime, timezone
import enum
from sqlalchemy import String, Integer, Text, ForeignKey, DateTime, Float, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login_manager

# --- Enums ---
class UserRole(enum.Enum):
    ADMIN = "Admin"
    ANALYST = "Analyst"
    VIEWER = "Viewer"

class SeverityLevel(enum.Enum):
    CRITICAL = "Critical"
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"

class VulnStatus(enum.Enum):
    OPEN = "Open"
    IN_PROGRESS = "In Progress"
    RESOLVED = "Resolved"
    CLOSED = "Closed"

# --- Models ---
class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(64), index=True, unique=True)
    email: Mapped[str] = mapped_column(String(120), index=True, unique=True)
    password_hash: Mapped[Optional[str]] = mapped_column(String(256))
    
    # Enum kullanımı ile veritabanı düzeyinde doğrulama
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.ANALYST)
    
    # timezone-aware datetime kullanımı
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    vulnerabilities: Mapped[List["Vulnerability"]] = relationship(back_populates="reporter")
    actions: Mapped[List["Action"]] = relationship(back_populates="user")

    def set_password(self, password: str) -> None:
        # Werkzeug 3.0+ ile scrypt varsayılandır, modern güvenlik standardıdır.
        self.password_hash = generate_password_hash(password, method='scrypt')

    def check_password(self, password: str) -> bool:
        if self.password_hash is None:
            return False
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return f'<User {self.username}>'

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

class Vulnerability(db.Model):
    __tablename__ = 'vulnerabilities'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150), index=True)
    description: Mapped[str] = mapped_column(Text)
    
    # Python enum ile veritabanında (CHECK constraint / Enum tipi) tutarlılık sağlanır
    severity: Mapped[SeverityLevel] = mapped_column(Enum(SeverityLevel), index=True)
    status: Mapped[VulnStatus] = mapped_column(Enum(VulnStatus), index=True, default=VulnStatus.OPEN)
    
    cvss_score: Mapped[Optional[float]] = mapped_column(Float)
    cve_id: Mapped[Optional[str]] = mapped_column(String(20))
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), 
        default=lambda: datetime.now(timezone.utc), 
        onupdate=lambda: datetime.now(timezone.utc)
    )
    
    reporter_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    reporter: Mapped["User"] = relationship(back_populates="vulnerabilities")
    actions: Mapped[List["Action"]] = relationship(back_populates="vulnerability", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f'<Vulnerability {self.title}>'

class Action(db.Model):
    __tablename__ = 'actions'

    id: Mapped[int] = mapped_column(primary_key=True)
    vulnerability_id: Mapped[int] = mapped_column(ForeignKey('vulnerabilities.id'))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    
    action_type: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(Text)
    
    timestamp: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    vulnerability: Mapped["Vulnerability"] = relationship(back_populates="actions")
    user: Mapped["User"] = relationship(back_populates="actions")

    def __repr__(self) -> str:
        return f'<Action {self.action_type} on Vuln {self.vulnerability_id}>'
      
