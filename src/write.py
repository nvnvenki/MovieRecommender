'''
Created on 15-Jan-2014

@author: venkatesh

description : This file reads the data from the files and writes to database
'''
import MySQLdb as db

class DbWriter:
    """ Class which writes data read from the file to the database """
    def __init__(self):
        """ Init method """
        self.connection = db.connect('localhost', 'root', 'hashedin', 'movies_test')
        self.cursor = self.connection.cursor()
        
    def  populate_genre(self, genre_file):
        """ Method which populates genre table """
        for genre_detail in genre_file.readlines():
            detail = genre_detail.split("|")
            query = "INSERT INTO genre (genre_id,genre_name) VALUES (" + detail[1].strip() + ",'" + detail[0].replace("'","") + "')"
            self.cursor.execute(query)
        self.connection.commit()
    
    def populate_movies(self, movies_file):
        """ Method which populates movies table """
        for movie_detail in movies_file.readlines():
            detail = movie_detail.strip().split("|")
            genre = self.__get_genres(detail[-19:])
            query = "INSERT INTO movies (movie_id,title,release_date,video_release_date,imdb_url,genres) VALUES (%s,'%s','%s','%s','%s','%s')" % (detail[0],detail[1].replace("'",""),detail[2],detail[3],detail[4].replace("%20"," "),detail[5])
            self.cursor.execute(query)
        self.connection.commit()
        
    def populate_users(self, users_file):
        """ Method which populates users table """
        
        for user_detail in users_file.readlines():
            detail = user_detail.split("|")
            
            query = "INSERT INTO user (user_id,age,gender,occupation,zipcode) VALUES (%s,%s,'%s','%s','%s')" % (detail[0], detail[1], detail[2], detail[3], detail[4].strip())
            self.cursor.execute(query)
        self.connection.commit()
    
    def populate_ratings(self, ratings_file):
        """ Method which populates ratings table """
        
        for rating_detail in ratings_file.readlines():
            detail = rating_detail.strip().split("\t")
            print detail
            
            
    def __del__(self):
        """ __del__ method """
        self.connection.close()
    
    def __get_genres(self,genre_data):
        """ Helper method to identify genre of the movie """
        actual_genres = ["unknown", "Action", "Adventure", "Animation",
              "Childrens", "Comedy", "Crime", "Documentary", "Drama", "Fantasy",
              "Film-Noir", "Horror", "Musical", "Mystery", "Romance","Sci-Fi" ,
              "Thriller", "War", "Western"]
        genre = ""
        for i in range(len(genre_data)):
            if genre_data[i] is "1":
                genre = genre + " " + actual_genres[i]     
        return genre
    
if __name__ == '__main__':
    try:
        dbw = DbWriter()
#       dbw.populate_genre(open("../data/genre.data"))
#       dbw.populate_users(open("../data/user.data"))
#       dbw.populate_movies(open("../data/movie.data"))
        dbw.populate_ratings(open("../data/ratings.data"))
        
    except db.Error, e:
        print "Exception occured: ", e.args[0], e.args[1]
        
        
        
