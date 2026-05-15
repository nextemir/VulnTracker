from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    # SQLAlchemy 2.x Mapped ve mapped_column syntax'ı
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(64), index=True, unique=True)
    email: Mapped[str] = mapped_column(String(120), index=True, unique=True)
    password_hash: Mapped[Optional[str]] = mapped_column(String(256))

    def __repr__(self) -> str:
        return f'<User {self.username}>'
