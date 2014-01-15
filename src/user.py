'''
Created on 15-Jan-2014

@author: venkatesh
description : User class representing user object
'''

class User:
    """ User class """
    def __init__(self, user_id, age, gender, occupation, zipcode):
        """ init method to construct user object """
        self.user_id = user_id
        self.age = age
        self.gender = gender
        self.occupation = occupation
        self.zipcode = zipcode
    
    def get_user_id(self):
        """ getter method to get the user id of the user """
        return self.user_id
    
    def get_age(self):
        """ getter method to get the age of the user """
        return self.age
    
    def get_gender(self):
        """ getter method to get the gender of the user """
        return self.gender
    
    def get_occupation(self):
        """ getter method to get the occupation of the user """
        return self.occupation
    
    def get_zipcode(self):
        """ getter method to get the zip code of the user """
        return self.zipcode
