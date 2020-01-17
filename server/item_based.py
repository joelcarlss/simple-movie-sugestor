from utils import *


def euclidean_for_every_movie(movie_a, other_movies):
    result = {}
    for movie_b in other_movies:
        if len(movie_b) > 0:
            result[movie_b[0]["movieId"]] = euclidean_compare(movie_a, movie_b)

    return result


# This one is used if only comparing two users
def euclidean_compare(movie_a, movie_b):
    count = 0
    sim = 0
    for val_a in movie_a:
        for val_b in movie_b:
            if val_a["userId"] == val_b["userId"]:
                sim += (float(val_a["rating"]) - float(val_b["rating"])) ** 2
                count += 1

    if count <= 0:
        return 0
    else:
        return 1/(1 + sim)


def calc_item_rating(movie_id, sim):
    arr = []
    sql = "select * from ratings WHERE NOT movieId = ANY (select movieId from ratings WHERE userId = %s)"
    stm = (movie_id,)
    all_ratings = query_db(sql, stm)
    for r in all_ratings:
        if not str(uid) == r["userId"]:
            new_r = {}
            for v in r:
                new_r[v] = r[v]
            w_score = round(float(r["rating"]) * sim[r["userId"]], 3)
            new_r["wScore"] = w_score
            arr.append(new_r)

    return arr
