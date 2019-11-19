import math


# This one is used if only comparing two users
def pearson_compare(user_a, user_b):
    count = 0
    sum1 = 0
    sum2 = 0
    sum1sq = 0
    sum2sq = 0
    p_sum = 0

    for rate_a in user_a:
        for rate_b in user_b:
            if rate_a["movieId"] == rate_b["movieId"]:
                a_score = float(rate_a["rating"])
                b_score = float(rate_b["rating"])

                sum1 += a_score
                sum2 += b_score
                sum1sq += a_score**2
                sum2sq += b_score**2
                p_sum += a_score * b_score

                count += 1

    if count == 0:
        return 0
    else:
        num = p_sum - ((sum1 * sum2) / count)
        den = math.sqrt((sum1sq - sum1**2 / count) * (sum2sq - sum2**2 / count))

        if num <= 0:
            return 0
        else:
            return num/den


def pearson(user_a, other_users):
    result = {}
    for rate_a in user_a:
        for rate_b in other_users:
            if rate_a["movieId"] == rate_b["movieId"]:
                if not rate_b["userId"] in result:
                    result[rate_b["userId"]] = {"sum1": 0, "sum2": 0, "sum1sq": 0, "sum2sq": 0, "pSum": 0, "count": 0}

                uid = rate_b["userId"]
                a_score = float(rate_a["rating"])
                b_score = float(rate_b["rating"])
                result[uid]["sum1"] += a_score
                result[uid]["sum2"] += b_score
                result[uid]["sum1sq"] += a_score**2
                result[uid]["sum2sq"] += b_score**2
                result[uid]["pSum"] += a_score * b_score
                result[uid]["count"] += 1

    for res in result:
        if result[res]["count"] == 0:
            result[res] = 0
        else:
            c = result[res]

            num = c["pSum"] - ((c["sum1"] * c["sum2"]) / c["count"])

            den = math.sqrt((c["sum1sq"] - c["sum1"]**2 / c["count"]) * (c["sum2sq"] - c["sum2"]**2 / c["count"]))

            if num <= 0:
                result[res] = 0
            else:
                result[res] = num/den

    return result


def pearson_for_every_user(user_a, other_users):
    result = {}
    for user_b in other_users:
        if len(user_b) > 0:
            result[user_b[0]["userId"]] = pearson_compare(user_a, user_b)

    return result


