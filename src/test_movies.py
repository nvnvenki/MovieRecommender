'''
Created on 16-Jan-2014

@author: venkatesh

Description : File contains Test cases of assignment

'''

from read import DBReader
from warmup import get_top_movie_by_genre
from warmup import get_top_movie_by_year
from warmup import get_top_movie_by_year_and_genre
from warmup import most_watched_movie
from warmup import most_watched_genre
from warmup import highest_rated_genre
from warmup import most_active_user
from recommender import Recommender


def main():
    """ Test cases """
    # --------------------------------------------------------------------
    #                      For warm up problems
    #---------------------------------------------------------------------
    reader = DBReader()
    all_genres = reader.read_genre()
    all_movies = reader.read_movies()
    all_ratings = reader.read_ratings()
    all_users = reader.read_users()
    
    
    movies = get_top_movie_by_genre(all_genres,all_movies,all_ratings)
    for each_genre in movies:
        print "=" * 40
        print "Top 5 movies of ", each_genre 
        print "=" * 40
        for each_movie in movies[each_genre]:
            print each_movie.get_title() , each_movie.ratings
        print "=" * 40
        
    movies = get_top_movie_by_year(all_genres,all_movies,all_ratings)
    for each_year in movies:
        print "=" * 40
        print "Top movies of ", each_year 
        print "=" * 40
        for each_movie in movies[each_year]:
            print each_movie.get_title() , each_movie.ratings
        print "=" * 40
        
    movies = get_top_movie_by_year_and_genre(all_genres,all_movies,all_ratings)
    
    for each_year in movies:
        print "=" * 40
        print "Year ", each_year 
        print "=" * 40
        for genres in movies[each_year]:
            for each_genre in genres:
                if len(genres[each_genre]) > 1:
                    for m in genres[each_genre]:
                        print m.get_title()
    
    # highest watched movies is based on no of users who rated that movie
    movie = most_watched_movie(all_movies, all_ratings) 
    print "most watched movie", movie.title
    print "=" * 40
    
    genre = most_watched_genre(all_movies, all_ratings, all_genres)  
    print "Most watched genre : ", genre
    
    genre = highest_rated_genre(all_movies, all_ratings, all_genres) 
    print "Highest rated genre: ", genre
    
    user = most_active_user(all_users, all_ratings)
    print "Most active user is user with user id : ", user
    
    print "-" * 40
    # --------------------------------------------------------------------
    #                      For Assignment
    #---------------------------------------------------------------------
    
    recommender = Recommender()
    movies_recommended = recommender.recommend_for(16660)
    if movies_recommended is not None:
        print "-" * 35
        print "Recommended top 5 movies for you!"
        print "-" * 35
        for movie in movies_recommended:
            print movie.get_title()
        print "-" * 35
    movies_recommended = recommender.recommend_for(166)
    if movies_recommended is not None:
        print "-" * 35
        print "Recommended top 5 movies for you!"
        print "-" * 35
        for movie in movies_recommended:
            print movie.get_title()
        print "-" * 35


if __name__ == '__main__':
    main()