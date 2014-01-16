'''
Created on 16-Jan-2014

@author: venkatesh

Description : Test cases for warm up problems

'''
import datetime
import unittest

from warmup import get_movie_for_id
from warmup import get_top_movie_by_genre
from warmup import get_top_movie_by_year
from warmup import get_top_movie_by_year_and_genre
from warmup import most_watched_movie
from warmup import most_watched_genre
from warmup import highest_rated_genre
from warmup import most_active_user
from warmup import get_ratings_dict
from warmup import get_movies_of_year
from warmup import get_movies_of_genre
from movie import Movie
from user import User


class Test(unittest.TestCase):
    """ Unit test class """
    
    def setUp(self):
        """ Generating all test data """
        unittest.TestCase.setUp(self)
        test_movies = [{"movie_id" : 1, "title": "Movie1", "release_date" : "01-Jan-2011", "imdb_url":"https://someurl.com", "genres":"Drama Thriller", "ratings":0},
                       {"movie_id" : 20, "title": "Movie2", "release_date" : "01-Jan-2010", "imdb_url":"https://someurl.com", "genres":"Mystery", "ratings":0},
                       {"movie_id" : 35, "title": "Movie3", "release_date" : "01-Jan-2010", "imdb_url":"https://someurl.com", "genres":"Drama", "ratings":0},
                       {"movie_id" : 3, "title": "Movie4", "release_date" : "01-Jan-2012", "imdb_url":"https://someurl.com", "genres":"Thriller Crime", "ratings":0},
                       {"movie_id" : 4, "title": "Movie5", "release_date" : "01-Jan-2012", "imdb_url":"https://someurl.com", "genres":"Crime", "ratings":0},
                       {"movie_id" : 10, "title": "Movie6", "release_date" : "01-Jan-2012", "imdb_url":"https://someurl.com", "genres":"Western", "ratings":0},
                       {"movie_id" : 11, "title": "Movie7", "release_date" : "01-Jan-2012", "imdb_url":"https://someurl.com", "genres":"War Crime", "ratings":0}]
        self.movies_objects = []
        for movies in test_movies:
            self.movies_objects.append(Movie(movies["movie_id"], movies["title"], movies["release_date"], movies["imdb_url"], movies["genres"], 0))
        
        self.test_ratings = [{'movie_id': 1, 'user_id': 1, 'rating': 10, 'timestamp' : datetime.datetime.fromtimestamp(891350008)},
                        {'movie_id': 20, 'user_id': 2, 'rating': 9, 'timestamp' : datetime.datetime.fromtimestamp(891350010)},
                        {'movie_id': 35, 'user_id': 3, 'rating': 7, 'timestamp' : datetime.datetime.fromtimestamp(891350012)},
                        {'movie_id': 3, 'user_id': 4, 'rating': 4, 'timestamp' : datetime.datetime.fromtimestamp(891350014)},
                        {'movie_id': 4, 'user_id': 5, 'rating': 5, 'timestamp' : datetime.datetime.fromtimestamp(891350016)},
                        {'movie_id': 10, 'user_id': 6, 'rating': 5, 'timestamp' : datetime.datetime.fromtimestamp(891350018)},
                        {'movie_id': 11, 'user_id': 7, 'rating': 6, 'timestamp' : datetime.datetime.fromtimestamp(891350020)},
                        {'movie_id': 1, 'user_id': 7, 'rating': 10, 'timestamp' : datetime.datetime.fromtimestamp(891350008)},
                        {'movie_id': 20, 'user_id': 6, 'rating': 9, 'timestamp' : datetime.datetime.fromtimestamp(891350010)},
                        {'movie_id': 35, 'user_id': 5, 'rating': 7, 'timestamp' : datetime.datetime.fromtimestamp(891350012)},
                        {'movie_id': 3, 'user_id': 4, 'rating': 4, 'timestamp' : datetime.datetime.fromtimestamp(891350014)},
                        {'movie_id': 4, 'user_id': 3, 'rating': 5, 'timestamp' : datetime.datetime.fromtimestamp(891350016)},
                        {'movie_id': 10, 'user_id': 2, 'rating': 5, 'timestamp' : datetime.datetime.fromtimestamp(891350018)},
                        {'movie_id': 11, 'user_id': 1, 'rating': 6, 'timestamp' : datetime.datetime.fromtimestamp(891350020)}]
        
        self.all_genres = {"unknown":0, "Action":1, "Adventure":2, "Animation":3, "Children's":4, "Comedy":5, "Crime":6, "Documentary":7, "Drama":8, "Fantasy":9, "Film-Noir":10,
                          "Horror":11, "Musical":12, "Mystery":13, "Romance":14, "Sci-Fi":15, "Thriller":16, "War":17, "Western":18}
        users_ = ["1 24 M technician 85711","2 53 F other 94043","3 23 M writer 32067","4 24 M technician 43537","5 33 F other 15213",
                  "6 42 M executive 98101","7 57 M administrator 91344","8 36 M administrator 05201","9 29 M student 01002","10 53 M lawyer 90703"]
        self.all_users = []
        for each_user in users_:
            each_user.split(" ")
            self.all_users.append(User(each_user[0], each_user[1], each_user[2], each_user[3], each_user[4]))
            

    def test_get_movie_for_id(self):     
        """ Test cases for get_movies_for_id method """
        self.assertEqual(get_movie_for_id(self.movies_objects, 10).get_title(), "Movie6")
        self.assertEqual(get_movie_for_id(self.movies_objects, 4).get_title(), "Movie5")
        self.assertIsNone(get_movie_for_id([], 100))
        self.assertIsNone(get_movie_for_id(None, 100))
        
    def test_get_movies_of_year(self): 
        """ Test cases for get_movies_of_year method """
        movies = get_movies_of_year(self.movies_objects, "2010")
        self.assertEqual(movies[0].get_title(), "Movie2")
        self.assertIsNone(get_movies_of_year([], 100))
        self.assertIsNone(get_movies_of_year(None, 100))
    
    def test_get_movies_of_genre(self):
        """ Test cases for get_movies_of_genre method """
        movies = get_movies_of_genre(self.movies_objects, "Drama")
        self.assertEqual(movies[0].get_title(), "Movie1")
        self.assertEqual(len(get_movies_of_genre(self.movies_objects, "Documentary")), 0)
        self.assertIsNone(get_movies_of_genre([], "Some"))
        self.assertIsNone(get_movies_of_genre(None, "Drama"))
        
    def test_get_top_movie_by_genre(self):
        """ Test cases for get_top_movies_by_genre method """
        movies = get_top_movie_by_genre(self.all_genres, self.movies_objects, self.test_ratings)
        self.assertEqual(movies['Mystery'][0].get_title(),"Movie2")
        self.assertIsNone(get_top_movie_by_genre([], [], [])) 
        self.assertIsNone(get_top_movie_by_genre([], None, [])) 
        
    def test_get_ratings_dict(self):
        """ Test cases for get_ratings_dict method """
        ratings = get_ratings_dict(self.test_ratings)
        self.assertEqual(ratings[1], 10)
        self.assertIsNone(get_ratings_dict([]))
        self.assertIsNone(get_ratings_dict(None))
    
    def test_most_active_user(self):
        """ Test cases for most_active_user method """
        user = most_active_user(self.all_users, self.test_ratings)
        self.assertEqual(user, 1)
        self.assertIsNone(most_active_user([], []))
        self.assertIsNone(most_active_user([], None))
    
    def test_highest_rated_genre(self):
        """ Test cases for highest_rated_genre method """
        highest_rated = highest_rated_genre(self.movies_objects, self.test_ratings, self.all_genres)
        self.assertEqual(highest_rated, "Mystery")
        self.assertIsNone(highest_rated_genre([], [], []))
        self.assertIsNone(highest_rated_genre(None, [], []))
    
    def test_get_top_movie_by_year_and_genre(self):
        """ Test cases for get_top_movie_by_year_and_genre method """
        movies = get_top_movie_by_year_and_genre(self.all_genres, self.movies_objects, self.test_ratings)
        self.assertEqual(movies['2011'][0]['Drama'][0].get_title(),"Movie1")
        self.assertIsNone(get_top_movie_by_year_and_genre([], None, []))
    
    def test_get_top_movie_by_year(self):
        """ Test cases for get_top_movie_by_year method """
        movies = get_top_movie_by_year(self.all_genres, self.movies_objects, self.test_ratings)
        self.assertEqual(movies["2012"][0].get_movie_id(), 11)
        self.assertIsNone(get_top_movie_by_year([], [], []))
        self.assertIsNone(get_top_movie_by_year(None, [], []))
        
    def test_most_watched_movie(self):
        """ Test cases for most_watched_movie method """
        movie = most_watched_movie(self.movies_objects, self.test_ratings)
        self.assertEqual(movie.get_title(), "Movie1")
        self.assertIsNone(most_watched_movie([], []))
        self.assertIsNone(most_watched_movie([], None))
        
    def test_most_watched_genre(self):
        """ Test cases for most_watched_movie method """
        genre = most_watched_genre(self.movies_objects, self.test_ratings, self.all_genres)
        self.assertEqual(genre, "Crime")
        self.assertIsNone(most_watched_genre([], [], []))
        self.assertIsNone(most_watched_genre([], [], None))
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()