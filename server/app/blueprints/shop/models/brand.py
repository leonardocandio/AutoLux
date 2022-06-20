from server.database import db
from server.app.models.super_models.time_model import TimeModel
from server.app.utils.web_scraping_cars import create_all_brands


class Brand(db.Model, TimeModel):
    __tablename__ = 'brands'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String, default='https://careerpartners.com.pe/wp-content/themes/consultix/images/no-image-found-360x260.png')

    @staticmethod
    def get_brands():
        if len(Brand.query.all()) == 0:
            create_all_brands(db, Brand)