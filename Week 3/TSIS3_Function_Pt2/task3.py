def category(movies):
    print('Category of your movie:')
    c = input()
    for i in range(len(movies)):
        if movies[i]['category'] == c:
            print(movies[i]['name'])