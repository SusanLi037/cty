def football_score(touchdowns, extra_points, two_point_conversions, field_goals, safeties):
    return(int(touchdowns * 6 + extra_points * 1 + two_point_conversions * 2 + field_goals * 3 + safeties * 2))
ravens_score = football_score(2, 2, 0, 3, 0)
print("The Baltimore Ravens scored {} points".format(ravens_score))
eagles_score = football_score(1, 0, 1, 1, 1)
print("The Philadelphia Eagles scored {} points".format(eagles_score))
