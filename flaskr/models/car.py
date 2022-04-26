from utils.db import db
from datetime import datetime
from .super_models.time_model import TimeModel


class Car(db.Model, TimeModel):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    make = db.Column(db.String(200), nullable=False)
    model = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String, default='https://careerpartners.com.pe/wp-content/themes/consultix/images/no-image-found-360x260.png')
    year = db.Column(db.Integer, nullable=False)
    horse_power = db.Column(db.Integer, default=0)
    price = db.Column(db.Float, nullable=False)



    
    