from utils.db import db
from datetime import datetime
from .super_models.time_model import TimeModel


class Car(db.Model, TimeModel):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    
    def __init__(self, name):
        self.name = name