def all_above_55(movies):
    above_55 = []
    for i in range(len(movies)):
        if movies[i]['imdb'] >= 5.5:
            above_55.append(movies[i])
    return above_55