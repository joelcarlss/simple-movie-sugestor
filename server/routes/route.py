from flask_restful import Resource, Api
from database import *
from model.pearson import *
from model.euclidean import *
from utils import *
from json import *


class Users(Resource):
    def get(self):
        result = query_db("select * from users")
        return {'res': result}  # Fetches first column that is Employee ID


class FindEuclidean(Resource):
    def get(self, user_id, amount):
        amount = int(float(amount))
        current_user, other_users = get_user_ratings_form_db(user_id)
        sim = euclidean_for_every_user(current_user, other_users)
        rating = calc_rating(user_id, sim)
        total_movie_score = calc_movie_score(rating, user_id)
        movie_results = get_movies_object(sim, total_movie_score)
        recommended = highest_values(movie_results, amount)
        return {'res': recommended}


class FindPearson(Resource):
    def get (self, user_id=1, amount=0):
        amount = int(float(amount))
        current_user, other_users = get_user_ratings_form_db(user_id)
        sim = pearson_for_every_user(current_user, other_users)
        rating = calc_rating(user_id, sim)
        total_movie_score = calc_movie_score(rating, user_id)
        movie_results = get_movies_object(sim, total_movie_score)
        recommended = highest_values(movie_results, amount)
        return {'res': recommended}



