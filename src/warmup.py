'''
Created on 15-Jan-2014

@author: venkatesh

description : This file contains solution to the warmup problems

'''
import operator

from read import DBReader

def get_top_movie_by_genre(all_genres,all_movies,all_ratings):
    """ Method to get the top movie of the genre """ 
    
    rating_dict = get_ratings_dict(all_ratings)
  
    top_movies = {}      
    for each_genre in all_genres:
        top_movies[each_genre] = []
        movies = get_movies_of_genre(all_movies, each_genre)
        for i in range(len(movies)):
            movies[i].ratings = rating_dict[movies[i].get_movie_id()]
            
        movies.sort(key=lambda x : x.ratings,reverse=True)
        top_movies[each_genre].extend(movies[:5])    
    return top_movies
    
def get_ratings_dict(all_ratings):
    """ Method to get the ratings of each movie (for movie id as key) """
    
    rating_dict = {}
    for rating in all_ratings:
        if rating_dict.has_key(rating['movie_id']):
            rating_dict[rating['movie_id']] = rating_dict[rating['movie_id']] + rating['rating']
        else:
            rating_dict[rating['movie_id']] = 0
    return rating_dict

def get_movie_for_id(movies, id):
    """ Helper method to get the movie object of the given id """
    return filter(lambda movie : movie.get_movie_id() == id, movies)[0]

def get_movies_of_genre(movies, genre):
    """ Helper method to get the movies of a particular genre """
    return filter(lambda movie: genre in movie.get_genres(),movies)
    
def get_movies_of_year(movies,year):
    """ Helper method to get the movies in a particular given year """
    return filter(lambda movie: movie.get_release_date()[-4:] == year, movies)
    
def get_top_movie_by_year(all_genres,all_movies,all_ratings):
    """ Method to get the top movies of the year """
    
    rating_dict = get_ratings_dict(all_ratings)

    years = []
    for movie in all_movies:
        years.append(movie.get_release_date()[-4:])
    years.remove('')
    years = set(years)
    years = list(years)
    
        
    top_movies = {}
    for each_year in years:
        top_movies[each_year] = []
        movies = get_movies_of_year(all_movies, each_year)
        for i in range(len(movies)):
            movies[i].ratings = rating_dict[movies[i].get_movie_id()]
        
        movies.sort(key=lambda x : x.ratings,reverse=True)
        top_movies[each_year].extend(movies[:2])    
    return top_movies   
                

def get_top_movie_by_year_and_genre(all_genres,all_movies,all_ratings):
    """ Method to get the top movies of the year and genre """
    
    rating_dict = get_ratings_dict(all_ratings)
    
    top_movies_by_year = get_top_movie_by_year(all_genres,all_movies,all_ratings)
    top_movies_by_year_and_genre = {}
    
    for each_year in top_movies_by_year:
        top_movies_by_year_and_genre[each_year] = []
        top_movies_by_year_and_genre[each_year].append(get_top_movie_by_genre(all_genres,top_movies_by_year[each_year],all_ratings))
    return top_movies_by_year_and_genre
    
def most_watched_movie(all_movies,all_ratings):
    """ Method to get the most watched movie """
    users_rating_dict = {}
    for rating in all_ratings:
        if users_rating_dict.has_key(rating['movie_id']):
            users_rating_dict[rating['movie_id']] = users_rating_dict[rating['movie_id']] + 1
        else:
            users_rating_dict[rating['movie_id']] = 0
            
    highest_watched_movie_id = max(users_rating_dict.iteritems(), key=operator.itemgetter(1))[0]
    return get_movie_for_id(all_movies, highest_watched_movie_id)

def most_watched_genre(all_movies, all_ratings, all_genres):
    """ Method to get the most watched genre """
    genre_rating_dict = {}
    
    for genre in all_genres:
        genre_rating_dict[genre] = 0
    
    for genre in all_genres:
        movies_of_genre = get_movies_of_genre(all_movies, genre)
        movie_ids_of_genre = map(lambda movie : movie.get_movie_id(),movies_of_genre)
        genre_rating_dict[genre] = genre_rating_dict[genre] + len(filter(lambda rating : rating['movie_id'] in movie_ids_of_genre, all_ratings))    
    return max(genre_rating_dict.iteritems(), key=operator.itemgetter(1))[0]

def highest_rated_genre(all_movies, all_ratings, all_genres):
    """ Method to get the highest rated genre """
    genre_rating_dict = {}
    
    for genre in all_genres:
        genre_rating_dict[genre] = 0
    
    for genre in all_genres:
        movies_of_genre = get_movies_of_genre(all_movies, genre)
        for movie in movies_of_genre:
            genre_rating_dict[genre] = genre_rating_dict[genre] + movie.get_ratings() 

    return max(genre_rating_dict.iteritems(), key=operator.itemgetter(1))[0]
    
def most_active_user(all_users, all_ratings):
    """ Method to get the most active user """
    user_id_dict = {}
    for rating in all_ratings:
        if user_id_dict.has_key(rating['user_id']):
            user_id_dict[rating['user_id']] = user_id_dict[rating['user_id']] + 1
        else:
            user_id_dict[rating['user_id']] = 0
    return max(user_id_dict.iteritems(), key=operator.itemgetter(1))[0]
    
    
if __name__ == '__main__':
    """ Test of methods """
    reader = DBReader()
    all_genres = reader.read_genre()
    all_movies = reader.read_movies()
    all_ratings = reader.read_ratings()
    all_users = reader.read_users()
    
    '''
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
        print "Top 5 movies of ", each_year 
        print "=" * 40
        for each_movie in movies[each_year]:
            print each_movie.get_title() , each_movie.ratings
        print "=" * 40
        
    movies = get_top_movie_by_year_and_genre(all_genres,all_movies,all_ratings)
    print movies
    for each_year in movies:
        print "=" * 40
        print "Year ", each_year 
        print "=" * 40
        for genres in movies[each_year]:
            for each_genre in genres:
                if len(genres[each_genre]) > 1:
                    for m in genres[each_genre]:
                        print m.get_title()
    '''
    # highest watched movies is based on no of users who rated that movie
    movie = most_watched_movie(all_movies, all_ratings) 
    print "most watched movie", movie.title
    print "=" * 40
    
    genre = most_watched_genre(all_movies, all_ratings, all_genres)  
    print "Most watched genre", genre
    
    genre = highest_rated_genre(all_movies, all_ratings, all_genres) 
    print "Highest rated genre", genre
    
    user = most_active_user(all_users, all_ratings)
    print "Most active user is user with user id ", user
     
    
    

    