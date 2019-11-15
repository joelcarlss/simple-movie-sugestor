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




# sim = euclidean_sim(1)
# rating = calc_rating(1, sim)
# recommended = highest_values(rating, 3)
# print(recommended)

api.add_resource(Users, '/users')  # Route_1
api.add_resource(FindEuclidean, '/find/euclidean/<user_id>/<amount>')
api.add_resource(FindPearson, '/find/pearson/<user_id>//<amount>')

if __name__ == '__main__':
    app.run(port='5002')

