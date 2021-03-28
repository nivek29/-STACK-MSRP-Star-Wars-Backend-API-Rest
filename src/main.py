"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, Character, Properties_Character, Profile, Properties_Profile, Planet, Properties_Planet
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/chracters',methods=['POST'])
def addChracter():
    request_body = request.get_json()
    chracter = Character(id=request_body["id"], name=request_body["name"])
    properties = Properties_Character(
                            id=request_body["id"],
                            character_id=request_body["id"],
                            height=request_body["height"], 
                            mass=request_body["mass"],
                            hair_color=request_body["hair_color"],
                            skin_color=request_body["skin_color"],
                            eye_color=request_body["eye_color"],
                            birth_year=request_body["birth_year"],
                            gender=request_body["gender"],
                            description= request_body["description"])
    print(request_body)

    db.session.add(chracter)
    db.session.add(properties)
    db.session.commit()

    return jsonify("All good"), 200
@app.route('/chracters/<int:id>',methods=['GET'])
def listChracter(id):
    responseCharacter = Character.query.get(id)
    responseCharacter = responseCharacter.serialize()
    return jsonify(responseCharacter), 200   
@app.route('/chracters/lista',methods=['GET'])
def listaCompleteChracters():
    completeChracters = Character.query.all()
    completeChracters_serialized = list(map(lambda data: data.serialize(), completeChracters))
    return jsonify(completeChracters_serialized),200
@app.route('/planets',methods=['POST'])
def addPlanet():
    request_planet = request.get_json()
    planet = Planet(id=request_planet["id"], name=request_planet["name"])
    propertiesPlanet = Properties_Planet(
                            id=request_planet["id"],
                            planet_id=request_planet["id"],
                            diameter=request_planet["diameter"], 
                            rotation_period=request_planet["rotation_period"],
                            orbital_period=request_planet["orbital_period"],
                            gravity=request_planet["gravity"],
                            population=request_planet["population"],
                            climate=request_planet["climate"],
                            terrain=request_planet["terrain"],
                            surface_water= request_planet["surface_water"])
    print(request_planet)

    db.session.add(planet)
    db.session.add(propertiesPlanet)
    db.session.commit()

    return jsonify("All good"), 200
@app.route('/planets/<int:id>',methods=['GET'])
def listPlanets(id):
    responsePlanet = Planet.query.get(id)
    responsePlanet = responsePlanet.serialize()
    return jsonify(responsePlanet), 200
@app.route('/planets/lista',methods=['GET'])
def listaCompletePlanets():
    completePlanets = Planet.query.all()
    completePlanets_serialized = list(map(lambda data: data.serialize(), completePlanets))
    return jsonify(completePlanets_serialized),200
@app.route('/profile',methods=['POST'])
def addProfile():
    request_profile = request.get_json()
    profile = Profile(id=request_profile["id"], email=request_profile["email"], password=request_profile["password"])
    propertiesProfile = Properties_Profile(
                            id=request_profile["id"],
                            profile_id=request_profile["id"],
                            name=request_profile["name"], 
                            age=request_profile["age"],
                            adress=request_profile["adress"])
    print(request_profile)

    db.session.add(profile)
    db.session.add(propertiesProfile)
    db.session.commit()

    return jsonify("All good"), 200
@app.route('/profile/<int:id>',methods=['GET'])
def listProfile(id):
    responseProfile = Profile.query.get(id)
    responseProfile = responseProfile.serialize()
    return jsonify(responseProfile), 200
@app.route('/profile/lista',methods=['GET'])
def listaCompleteProfile():
    completeProfile = Profile.query.all()
    completeProfile_serialized = list(map(lambda data: data.serialize(), completeProfile))
    return jsonify(completeProfile_serialized),200



# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
