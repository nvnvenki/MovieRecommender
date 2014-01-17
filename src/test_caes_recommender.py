'''
Created on 17-Jan-2014

@author: venkatesh
'''
import unittest
import datetime

from recommender import Recommender
from movie import Movie
from user import User
import recommender


class Test(unittest.TestCase):
    """ Test class for Recommender """
    
    def setUp(self):
        """ initial set up of Test cases """
        unittest.TestCase.setUp(self)
        self.recommender = Recommender()
        test_movies = [{"movie_id" : 1, "title": "Movie1", "release_date" : "01-Jan-2011", "imdb_url":"https://someurl.com", "genres":"Drama Thriller", "ratings":0},
                       {"movie_id" : 20, "title": "Movie2", "release_date" : "01-Jan-2010", "imdb_url":"https://someurl.com", "genres":"Mystery", "ratings":0},
                       {"movie_id" : 35, "title": "Movie3", "release_date" : "01-Jan-2010", "imdb_url":"https://someurl.com", "genres":"Drama", "ratings":0},
                       {"movie_id" : 3, "title": "Movie4", "release_date" : "01-Jan-2012", "imdb_url":"https://someurl.com", "genres":"Thriller Crime", "ratings":0},
                       {"movie_id" : 4, "title": "Movie5", "release_date" : "01-Jan-2012", "imdb_url":"https://someurl.com", "genres":"Crime", "ratings":0},
                       {"movie_id" : 10, "title": "Movie6", "release_date" : "01-Jan-2012", "imdb_url":"https://someurl.com", "genres":"Western", "ratings":0},
                       {"movie_id" : 11, "title": "Movie7", "release_date" : "01-Jan-2012", "imdb_url":"https://someurl.com", "genres":"War Crime", "ratings":0}]
        movies_objects = []
        for movies in test_movies:
            movies_objects.append(Movie(movies["movie_id"], movies["title"], movies["release_date"], movies["imdb_url"], movies["genres"], 0))
        
        test_ratings = [{'movie_id': 1, 'user_id': 1, 'rating': 10, 'timestamp' : datetime.datetime.fromtimestamp(891350008)},
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
        
        all_genres = {"unknown":0, "Action":1, "Adventure":2, "Animation":3, "Children's":4, "Comedy":5, "Crime":6, "Documentary":7, "Drama":8, "Fantasy":9, "Film-Noir":10,
                          "Horror":11, "Musical":12, "Mystery":13, "Romance":14, "Sci-Fi":15, "Thriller":16, "War":17, "Western":18}
        users_ = ["1 24 M technician 85711","2 53 F other 94043","3 23 M writer 32067","4 24 M technician 43537","5 33 F other 15213",
                  "6 42 M executive 98101","7 57 M administrator 91344","8 36 M administrator 05201","9 29 M student 01002","10 53 M lawyer 90703"]
        all_users = []
        for each_user in users_:
            each_user.split(" ")
            all_users.append(User(each_user[0], each_user[1], each_user[2], each_user[3], each_user[4]))
        
        self.recommender.all_ratings = test_ratings
        self.recommender.all_movies = movies_objects
        self.recommender.all_users = all_users
        self.recommender.all_genre = all_genres
    
        
    def test_recommend_for(self):
        """ test case for recommend_for """
        movie = self.recommender.recommend_for("h")
        self.assertIsNone(movie)
        
        movie = self.recommender.recommend_for(100)
        self.assertIsNone(movie)
        
        movie = self.recommender.recommend_for(1)
        self.assertEqual(movie[0].get_title(), "Movie2")
        
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()