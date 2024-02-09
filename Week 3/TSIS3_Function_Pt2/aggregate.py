from task1 import is_above_55
from task2 import all_above_55
from task3 import category
from task4 import aver_movie_imdb
from task5 import aver_category_imdb

movies = [ 
    { "name": "Usual Suspects", "imdb": 7.0, "category": "Thriller" }, 
    { "name": "Hitman", "imdb": 6.3, "category": "Action" }, 
    { "name": "Dark Knight", "imdb": 9.0, "category": "Adventure" }, 
    { "name": "The Help", "imdb": 8.0, "category": "Drama" }, 
    { "name": "The Choice", "imdb": 6.2, "category": "Romance" }, 
    { "name": "Colonia", "imdb": 7.4, "category": "Romance" }, 
    { "name": "Love", "imdb": 6.0, "category": "Romance" }, 
    { "name": "Bride Wars", "imdb": 5.4, "category": "Romance" }, 
    { "name": "AlphaJet", "imdb": 3.2, "category": "War" }, 
    { "name": "Ringing Crime", "imdb": 4.0, "category": "Crime" }, 
    { "name": "Joking muck", "imdb": 7.2, "category": "Comedy" }, 
    { "name": "What is the name", "imdb": 9.2, "category": "Suspense" }, 
    { "name": "Detective", "imdb": 7.0, "category": "Suspense" }, 
    { "name": "Exam", "imdb": 4.2, "category": "Thriller" }, 
    { "name": "We Two", "imdb": 7.2, "category": "Romance" } 
    ]

#Task 1
print(is_above_55(movies))
#Task 2
print(all_above_55(movies))
#Task 3
print(category(movies))
#Task 4
movie_list = ['Hitman', 'We Two']
print(aver_movie_imdb(movie_list, movies))
#Task 5
category = ['Thriller']
print(aver_category_imdb(category, movies))