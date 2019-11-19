import csv
from database import mycursor
from model import *
import json


# Returns arrays with objects
def query_db(query, args=(), one=False):
    mycursor.execute(query, args)
    r = [dict((mycursor.description[i][0], value)
              for i, value in enumerate(row)) for row in mycursor.fetchall()]
    return (r[0] if r else None) if one else r


def get_rating_from_db(uid):
    other = query_db("select distinct userId, movieId, rating from ratings WHERE NOT userId = %s", (uid,))
    selected = query_db("select distinct userId, movieId, rating from ratings WHERE userId = %s;", (uid,))
    return selected, other


def get_user_ratings_form_db(uid):
    selected = query_db("select distinct userId, movieId, rating from ratings WHERE userId = %s;", (uid,))
    other_users = []
    users = query_db("select * from users WHERE NOT userId = %s", (uid,))
    for user in users:
        rating = query_db("select distinct userId, movieId, rating from ratings WHERE userId = %s;", (user["userId"],))
        other_users.append(rating)

    return selected, other_users




def get_movies_object(sim, w_score):
    result = []
    movies = query_db("select * from movies")
    for movie in movies:
        if str(movie["id"]) in w_score:
            movie["w_score"] = round((w_score[str(movie["id"])] / sim), 3)
            if movie["w_score"] >= 0:
                result.append(movie)

    return result


def calc_rating(uid, sim):
    arr = []
    sql = "select * from ratings WHERE NOT movieId = ANY (select movieId from ratings WHERE userId = %s)"
    stm = (uid,)
    all_ratings = query_db(sql, stm)
    i = 0
    for r in all_ratings:
        if not str(uid) == r["userId"]:
            new_r = {}
            for v in r:
                new_r[v] = r[v]
            w_score = float(r["rating"]) * sim[r["userId"]]
            new_r["wScore"] = w_score
            arr.append(new_r)
        i += 1

    return arr


def highest_values(arr, amount):
    arr.sort(key=last_val, reverse=True)
    if len(arr) <= amount or amount <= 0:
        return arr
    else:
        return arr[0:amount:]


def last_val(arr):
    return arr["w_score"]


# Returns the added weighted score for all movies
def calc_movie_score(arr, user_id):
    movies = {}
    for k in arr:
        if user_id != k["userId"]:
            if not k["movieId"] in movies:
                movies[k["movieId"]] = 0
            movies[k["movieId"]] += k["wScore"]

    return movies


def calc_added_sim(sim):
    total = 0
    for val in sim:
        total += sim[val]

    return total

