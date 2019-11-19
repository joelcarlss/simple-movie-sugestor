# This one is for comparing one user with many
def euclidean(user_a, users):
    result = {}
    for val_a in user_a:
        for val_b in users:
            if val_a["movieId"] == val_b["movieId"]:
                if not val_b["userId"] in result:
                    result[val_b["userId"]] = {"sim": 0, "count": 0}

                result[val_b["userId"]]["sim"] += (round(float(val_a["rating"]), 2) - round(float(val_b["rating"]), 2))**2
                result[val_b["userId"]]["count"] += 1

    for a in result:
        if result[a]["count"] == 0:
            result[a] = 0
        else:
            result[a] = round(1/(1 + result[a]["sim"]), 3)

    return result


def euclidean_for_every_user(user_a, other_users):
    result = {}
    for user_b in other_users:
        if len(user_b) > 0:
            result[user_b[0]["userId"]] = euclidean_compare(user_a, user_b)

    return result


# This one is used if only comparing two users
def euclidean_compare(user_a, user_b):
    count = 0
    sim = 0
    for val_a in user_a:
        for val_b in user_b:
            if val_a["movieId"] == val_b["movieId"]:
                sim += (float(val_a["rating"]) - float(val_b["rating"])) ** 2
                count += 1

    if count <= 0:
        return 0
    else:
        return 1/(1 + sim)

