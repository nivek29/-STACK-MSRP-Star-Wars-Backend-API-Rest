from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    properties = db.relationship('Properties_Character', backref='character', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "properties": list(map(lambda det_properties: det_properties.serialize(),self.properties))
            # do not serialize the password, its a security breach
        }
class Properties_Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), nullable=False)
    height = db.Column(db.Float,nullable=False)
    mass = db.Column(db.Float,nullable=False)
    hair_color = db.Column(db.String(60),nullable=False)
    skin_color = db.Column(db.String(60),nullable=False)
    eye_color = db.Column(db.String(60),nullable=False)
    birth_year = db.Column(db.String(25),nullable=False)
    gender = db.Column(db.String(50),nullable=False)
    description = db.Column(db.String(250),nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "height":self.height,
            "description": self.description
            # do not serialize the password, its a security breach
        }
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120), nullable=False)
    profile = db.relationship('Properties_Profile', backref='profile', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "properties": list(map(lambda det_properties: det_properties.serialize(),self.profile))
            # do not serialize the password, its a security breach
        }
class Properties_Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    adress = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "adress": self.adress,
            # do not serialize the password, its a security breach
        }
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    properties = db.relationship('Properties_Planet', backref='planet', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "properties": list(map(lambda det_properties: det_properties.serialize(),self.properties))
            # do not serialize the password, its a security breach
        }
class Properties_Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)
    diameter = db.Column(db.Float, nullable=False)
    rotation_period = db.Column(db.Integer, nullable=False)
    orbital_period = db.Column(db.Integer, nullable=False)
    gravity = db.Column(db.String(50), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    climate = db.Column(db.String(50), nullable=False)
    terrain = db.Column(db.String(50), nullable=False)
    surface_water = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            # do not serialize the password, its a security breach
        }