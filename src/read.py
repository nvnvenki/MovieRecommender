'''
Created on 15-Jan-2014

@author: venkatesh

description : This file is to read the data from the database
'''

import MySQLdb as db
import datetime

from movie import Movie
from user import User

class DBReader:
    """ Reader class which reads from the database """
    def __init__(self):
        """ init method to construct DBReader object """
        self.connection = db.connect('localhost', 'root', 'hashedin', 'movies_test')
        self.cursor = self.connection.cursor(db.cursors.DictCursor)
    
    def read_genre(self):
        """ Method to read genre from the database """
        all_genres = {}
        self.cursor.execute("SELECT * FROM genre")
        rows = self.cursor.fetchall()
        for row in rows:
            all_genres[row['genre_name']] = int(row['genre_id'])
        return all_genres
    
    def read_users(self):
        """ Method to read the user data from the database """
        all_users = []
        self.cursor.execute("SELECT * FROM user")
        rows = self.cursor.fetchall()
        for row in rows:
            all_users.append(User(row["user_id"], row["age"], ["gender"], row["occupation"], row["zipcode"]))
        
        return all_users
    
    def read_movies(self):
        """ Method to read the movies data from the database """
        all_movies = []
        self.cursor.execute("SELECT * FROM movies")
        rows = self.cursor.fetchall()
        for row in rows:
            all_movies.append(Movie(row["movie_id"], row["title"], row["release_date"], row["imdb_url"], row["genres"], 0))
#            break                 
        return all_movies
    
    def read_ratings(self):
        """ Method to read ratings data stored in the database """
        all_ratings = []
        self.cursor.execute("SELECT * FROM ratings")
        rows = self.cursor.fetchall()
        for row in rows:
            all_ratings.append({'movie_id':int(row['movie_id']), 'user_id':int(row['user_id']), 'rating': int(row['rating']), 'timestamp' : datetime.datetime.fromtimestamp(int(row['timestamp']))})  
        return all_ratings     
    
    def __del__(self):
        """ Destructor method """
        self.connection.close()
        
if __name__ == '__main__':
    try:
        dbr = DBReader()
    #    print dbr.read_genre()
        a = dbr.read_movies()
        print a[0].get_title(), len(a)
        
        b = dbr.read_ratings()
#        print b[0]['timestamp'].year
    except db.Error, e:
        print "Exception occured: ", e.args[0], e.args[1]