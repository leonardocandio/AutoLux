from utils.db import db
from .super_models.time_model import TimeModel


class Brand(db.Model, TimeModel):
    __tablename__ = 'brands'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String, default='https://careerpartners.com.pe/wp-content/themes/consultix/images/no-image-found-360x260.png')

