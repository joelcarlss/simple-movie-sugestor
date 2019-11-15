import csv
from database import mycursor
from model import *
import json

def read_movies():
    sql = "INSERT INTO movies (id, title, year) VALUES (%s, %s, %s)"
    with open('./movies_large/movies.csv', 'r') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=';')
        for row in readcsv:
            print(row[0].isnumeric())
            if row[0].isnumeric():
                val = (row[0], row[1], row[2])
                mycursor.execute(sql, val)


def read_users():
    sql = "INSERT INTO users (userId, name) VALUES (%s, %s)"
    with open('./movies_large/users.csv') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=';')
        for row in readcsv:
            if row[0].isnumeric():
                val = (row[0], row[1])
                mycursor.execute(sql, val)


def read_ratings():
    sql = "INSERT INTO ratings (userId, movieId, rating) VALUES (%s, %s, %s)"
    with open('./movies_large/ratings.csv') as csvfile:
        readcsv = csv.reader(csvfile, delimiter=';')
        for row in readcsv:
            if row[0].isnumeric():
                val = (row[0], row[1], row[2])
                mycursor.execute(sql, val)


def query_db(query, args=(), one=False):
    mycursor.execute(query, args)
    r = [dict((mycursor.description[i][0], value)
              for i, value in enumerate(row)) for row in mycursor.fetchall()]
    return (r[0] if r else None) if one else r


def get_rating_from_db(uid):
    other = query_db("select distinct userId, movieId, rating from ratings WHERE NOT userId = %s", (uid,))
    selected = query_db("select distinct userId, movieId, rating from ratings WHERE userId = %s;", (uid,))
    return selected, other


def get_movies_object(sim, w_score):
    result = []
    movies = query_db("select * from movies")
    for movie in movies:
        if str(movie["id"]) in w_score:
            movie["w_score"] = (w_score[str(movie["id"])] / sim)
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
            w_score = round(float(r["rating"]) * sim[r["userId"]], 3)
            new_r["wScore"] = w_score
            arr.append(new_r)
        i += 1

    return arr


def highest_values(arr, amount):
    amount = amount+1
    arr.sort(key=last_val)
    return arr[:-amount:-1]


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

    # print(movies)
    return movies


def calc_added_sim(sim):
    total = 0
    for val in sim:
        total += sim[val]

    return total

