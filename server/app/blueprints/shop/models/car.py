from server.app.models.super_models.time_model import TimeModel
from server.database import db
from server.app.utils.web_scraping_cars import create_all_cars


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

    @staticmethod
    def create_first_car():
        car = {
            'name': 'Toyota yaris 2022',
            'image_url': 'https://careerpartners.com.pe/wp-content/themes/consultix/images/no-image-found-360x260.png',
            'price': 9999,
            'description': 'Toyota yaris 2022',
            'brand': 'Toyota',
            'model': 'yaris',
            'category': 'Camioneta',
            'year': 2022,
            'year_production': 2000,
            'milage': 2000,
            'transmission': '',
            'fuel': 'test_fuel',
            'engine_displacement': 'test_enigne',
            'doors': 4,
            'drivetrain': 'test_drive',
            'color': 'negro',
            'cylinders': 1,
            'location': 'San Borja'
        }
        try:
            db.session.add(car)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(e)
        finally:
            db.session.close()


    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "image_url": self.image_url,
            "price": self.price,
            "description": self.description,
            "brand" :self.brand,
            "model" :self.model,
            "category" :self.category,
            "year" :self.year,
            "year_production" :self.year_production, 
            "mileage" :self.mileage,
            "transmission" :self.transmission,
            "fuel" :self.fuel,
            "engine_displacement" :self.engine_displacement ,
            "doors" :self.doors,
            "drivetrain" :self.drivetrain,
            "color" :self.color,
            "cylinders" :self.cylinders,
            "location" :self.location
        }
