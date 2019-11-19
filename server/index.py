from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from json import dumps
from flask_cors import CORS
from utils import *
from routes.route import *
from database import *

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(Users, '/users')  # Route_1
api.add_resource(FindEuclidean, '/find/movies/euclidean/<user_id>/<amount>')
api.add_resource(FindPearson, '/find/movies/pearson/<user_id>/<amount>')
api.add_resource(FindEuclideanUsers, '/find/users/euclidean/<user_id>/<amount>')
api.add_resource(FindPearsonUsers, '/find/users/pearson/<user_id>/<amount>')

if __name__ == '__main__':
    app.run(port='5002')

