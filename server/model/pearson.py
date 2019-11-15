import math


def pearson(user_a, other_users):
    count = 0
    result = {}
    for rate_a in user_a:
        for rate_b in other_users:
            if rate_a["movieId"] == rate_b["movieId"]:
                if not rate_b["userId"] in result:
                    print("Created result slot for user ", rate_b["userId"])
                    result[rate_b["userId"]] = {"sum1": 0, "sum2": 0, "sum1sq": 0, "sum2sq": 0, "pSum": 0, "count": 0}

                uid = rate_b["userId"]
                a_score = float(rate_a["rating"])
                b_score = float(rate_b["rating"])

                result[uid]["sum1"] += a_score
                result[uid]["sum2"] += b_score
                result[uid]["sum1sq"] += a_score**2
                result[uid]["sum2sq"] += b_score**2
                result[uid]["pSum"] += a_score + b_score
                result[uid]["count"] += 1

    for res in result:
        if result[res]["count"] == 0:
            result[res] = 0
        else:
            c = result[res]
            num = c["pSum"] - (c["sum1"] * c["sum2"] / c["count"])
            den = math.sqrt((c["sum1sq"] - c["sum1"]**2 / c["count"]) * (c["sum2sq"] - c["sum2"]**2 / c["count"]))

            print(num, "/", den)
            result[res] = num/den
            print(result[res])

    print(result)
    return result
