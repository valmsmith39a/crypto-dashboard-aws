from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json
import os

database_path = os.getenv("DATABASE_URL")

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Token(db.Model):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    symbol = Column(String(120))
    price = Column(Integer)
    sentiment_score = Column(Integer)
