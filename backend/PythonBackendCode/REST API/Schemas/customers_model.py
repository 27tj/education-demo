from ...HTTPResolver import db
from flask_login import UserMixin
import sqlalchemy as sa

class Customers(db.Model, UserMixin):
    uuid = sa.Column(sa.VARBINARY(16), primary_key=True)
    email = sa.Column(sa.VARCHAR(200), unique=True)
    password = sa.Column(sa.VARCHAR(200))
    name = sa.Column(sa.VARCHAR(200))
    address = sa.Column(sa.TEXT)
    age = sa.Column(sa.INTEGER)