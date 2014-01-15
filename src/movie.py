'''
Created on 15-Jan-2014

@author: venkatesh
description: class representing a movie

'''

class Movie:
    """ Class Movie """
    def __init__(self, movie_id, title, release_date, imdb_url, genres,ratings):
        """ constructor for movie object """
        self.movie_id = movie_id
        self.title = title
        self.release_date = release_date
        self.imdb_url = imdb_url
        self.genres = genres.split(" ")
        self.ratings = ratings
    
    def get_ratings(self):
        """ Getter method to get the rating of the movie """
        return self.ratings
        
    def get_genres(self):
        """ getter method to get the genre of the movie """
        return self.genres
    
    def get_title(self):
        """ getter method to get the title of the movie """
        return self.title
    
    def get_release_date(self):
        """ getter method to get the release date of the movie """
        return self.release_date
    
    def getimdb_url(self):
        """ getter method to get the imdb url of the movie """
        return self.imdb_url
    
    def get_movie_id(self):
        """ getter method to get the movie id of the movie """
        return self.movie_id
    
