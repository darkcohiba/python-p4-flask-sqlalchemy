from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class Owner(db.Model):
#     __tablename__ = 'owners'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, unique=True)

#     pets = db.relationship('Pet', backref='owner')

#     def __repr__(self):
#         return f'<Pet Owner {self.name}>'

# class Pet(db.Model):
#     __tablename__ = 'pets'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String)
#     species = db.Column(db.String)

#     owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))

#     def __repr__(self):
#         return f'<Pet {self.name}, {self.species}>'

from datetime import datetime

class Hike(db.Model):
    __tablename__ = 'hikes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    description = db.Column(db.String)
    hikeImageUrl = db.Column(db.String)
    hikeLink = db.Column(db.String)
    startDateTime = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)
    endDateTime = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    def __repr__(self):
        return f'<Hike {self.name}, {self.description}. {self.startDateTime} and {self.endDateTime}>'