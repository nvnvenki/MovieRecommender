'''
Created on 16-Jan-2014

@author: venkatesh
description: This file contains the class which recommends 5 movies to the user given his user id

'''

import operator

from read import DBReader


class Recommender:
    """ Recommender class which suggests 5 movies to the user with the id """
    def __init__(self):
        """ init method which initialises the object """
        reader = DBReader()
        self.all_movies = reader.read_movies() 
        self.all_ratings = reader.read_ratings()
        self.all_genre = reader.read_genre()
        self.all_users = reader.read_users()
    
    def recommend_for(self, user_id):
        """ method which recommends movies to users giver their use id """
        # Steps
        # 1. Find to which genres the user has rated most
        # 2. Return top 5 movies in that genre
        
        self.user_ids = [int(user.get_user_id()) for user in self.all_users]
        
        if self.all_movies and self.all_ratings and self.all_genre and self.all_users and len(self.all_movies) < 1 and len(self.all_ratings) < 1 and len(self.all_genre) < 1 and len(self.all_users) < 1:
            print "No data"
            return None
        
        
        if user_id not in self.user_ids:
            print "User with user id %s is not a valid user" % str(user_id)
            return None
        
        rated_by_this_user = filter(lambda rating: rating['user_id'] == user_id, self.all_ratings)
        movies_watched_by_this_user = map(lambda rating: rating['movie_id'] , rated_by_this_user)
        
        genres_ratings_dict = {}
        for genre in self.all_genre:
            genres_ratings_dict[genre]  = 0
            
        for movie_ids in movies_watched_by_this_user:
            movie = self.___get_movie_for_id(movie_ids)
            for each_genre in movie.get_genres()[1:]:
                genres_ratings_dict[each_genre] = genres_ratings_dict[each_genre] + movie.get_ratings()
       
        max_rated_genre_by_user = max(genres_ratings_dict.iteritems(), key=operator.itemgetter(1))[0]
        movies_of_max_rated_genre =  self.__get_top_movie_by_genre()[max_rated_genre_by_user]
        return filter(lambda movie: movie.get_movie_id() not in movies_watched_by_this_user ,movies_of_max_rated_genre)[:5]
    
    def ___get_movie_for_id(self, id_):
        """ Helper method to get the movie object of the given id """
        return filter(lambda movie : movie.get_movie_id() == id_, self.all_movies)[0]
    
    def __get_top_movie_by_genre(self):
        """ Method to get the top movie of the genre """ 
        
        rating_dict = self.__get_ratings_dict()
      
        top_movies = {}      
        for each_genre in self.all_genre:
            top_movies[each_genre] = []
            movies = self.__get_movies_of_genre(each_genre)
            for i in range(len(movies)):
                movies[i].ratings = rating_dict[movies[i].get_movie_id()]
                
            movies.sort(key=lambda x : x.ratings,reverse=True)
            top_movies[each_genre].extend(movies)    
        return top_movies
    
    def __get_ratings_dict(self):
        """ Method to get the ratings of each movie (for movie id as key) """ 
        rating_dict = {}
        for rating in self.all_ratings:
            if rating_dict.has_key(rating['movie_id']):
                rating_dict[rating['movie_id']] = rating_dict[rating['movie_id']] + rating['rating']
            else:
                rating_dict[rating['movie_id']] = 0
        return rating_dict
    
    def __get_movies_of_genre(self, genre):
        """ Helper method to get the movies of a particular genre """
        return filter(lambda movie: genre in movie.get_genres(),self.all_movies)
    
if __name__ == "__main__":
    
    recommender = Recommender()
    movies_recommended = recommender.recommend_for(10)
    if movies_recommended is not None:
        print "-" * 35
        print "Recommended top 5 movies for you!"
        print "-" * 35
        for movie in movies_recommended:
            print movie.get_title()
        print "-" * 35




        