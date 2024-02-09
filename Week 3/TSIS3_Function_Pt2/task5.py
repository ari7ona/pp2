def aver_category_imdb(cat, movies):
    imdb_sum = 0
    count = 0

    for movie in movies:
        if movie["category"] in cat:
            imdb_sum += movie["imdb"]
            count += 1

    if count == 0:
        return 0

    aver_imdb = imdb_sum / count
    return round(aver_imdb, 1)