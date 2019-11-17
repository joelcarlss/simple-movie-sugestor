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

