from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class PrivateKey(db.Model):
    __tablename__ = 'Private_Keys'
    hash_key = db.Column(db.String(100), nullable=False, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
