from utils.db import db
from datetime import datetime

class Car(db.Model):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    last_updated = db.Column(db.DateTime)

    def __init__(self, created_at=datetime.now() , last_updated=datetime.now()):
        self.created_at = created_at
        self.last_updated = last_updated