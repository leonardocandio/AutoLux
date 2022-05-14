from app.models.super_models.time_model import TimeModel
from database import db
from app.utils.web_scraping_cars import create_all_cars


class Car(db.Model, TimeModel):
    __tablename__ = 'cars'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    image_url = db.Column(db.String,
                          default='https://careerpartners.com.pe/wp-content/themes/consultix/images/no-image-found-360x260.png')
    price = db.Column(db.Integer)  ## ENTERO POSITIVO

    description = db.Column(db.String(2000))
    brand = db.Column(db.String(200), nullable=False)
    model = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(500))
    year = db.Column(db.Integer, default=0)  ## ENTERO POSITIVO
    year_production = db.Column(db.Integer, default=0)  ## ENTERO POSITIVO
    mileage = db.Column(db.Integer, default=0)  # kilometraje ## ENTERO POSITIVO
    transmission = db.Column(db.String(200))  # transmission
    fuel = db.Column(db.String(200))  # tipo de combustible
    engine_displacement = db.Column(db.String(200))  # cilindrada
    doors = db.Column(db.Integer, default=0)  ## ENTERO POSITIVO
    drivetrain = db.Column(db.String(200))  # tipo de Traccion
    color = db.Column(db.String(200))
    cylinders = db.Column(db.Integer, default=0)  # numero de cilindros ## ENTERO POSITIVO
    location = db.Column(db.String(200))

    @staticmethod
    def get_cars():
        if len(Car.query.all()) == 0:
            create_all_cars(db, Car)
