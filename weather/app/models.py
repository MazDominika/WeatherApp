from app import db, login
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True, nullable=False)
    password: so.Mapped[Optional[str]] = so.mapped_column(sa.String(64), index=True,
                                                unique=True, nullable=False)
    rememberme: so.Mapped[bool] = so.mapped_column(sa.Boolean)

    def check_password(self, password):
        return self.password == password 

@login.user_loader
def loader_user(id):
    return db.session.get(User, int(id))


class Measurments(db.Model):
    
    temperature: so.Mapped[float] = so.mapped_column(sa.Float)
    pressure: so.Mapped[float] = so.mapped_column(sa.Float)
    humidity: so.Mapped[float] = so.mapped_column(sa.Float)
    date = so.mapped_column(sa.DateTime, primary_key=True)