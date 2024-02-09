def is_above_55(movies):
    print('Name of your movie:')
    name = input()
    for i in range(len(movies)):
        if movies[i]['imdb'] >= 5.5 and movies[i]['name'] == name:
            return True