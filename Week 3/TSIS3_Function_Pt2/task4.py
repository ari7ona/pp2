def aver_movie_imdb(movie_list, movies):
    imdb_sum = 0
    count = 0

    for movie in movies:
        if movie["name"] in movie_list:
            imdb_sum += movie["imdb"]
            count += 1

    if count == 0:
        return 0

    aver_imdb = imdb_sum / count
    return round(aver_imdb, 1)