import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from pprint import pprint

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:47112/?authSource=AAC' % (username, password))
        self.database = self.client['AAC']
        
        
    def create(self, data):
        # Checks if data parameter is an empty value
        if data:
            self.database.animals.insert(data) # data should be dictionary
        else:
            raise Exception("Nothing to save because data parameter is empty")
            
        # Checks if data was succesfully inserted
        if self.database.animals.find(data):
            return "Document successfully inserted!"
        else:
            return "Document not inserted."
           
        
    def read(self, data):   
        # If user inputs key/value pair, search for match
        # Otherwise, return all documents or exception
        if data:
            # Finds first document that matches query
            target = self.database.animals.find(data)
            
            # If list is not empty/document matching query exists, prints request
            # Otherwise, raises exception
            if target: 
                return target
            else:
                raise Exception("Document with specified key/value pair not in database")
        else:
            # Creates a list of all documents matching query
            target = self.database.animals.find({})
            if target: 
                return target
            else:
                raise Exception("No documents in database")
            
            
    def update(self, target, data):
        # If parameters are not empty, begins update process
        # Otherwise, error occurs
        if target and data:
            result = self.database.animals.update_one(target, {"$set" : data})
            # If update target is found, prints raw JSON output
            # Otherwise, error occurs
            if result.matched_count > 0:
                return result.raw_result
            else:
                raise Exception("Document with specified key/value pair not in database")
        else:
            raise Exception("Nothing to update because one or both parameters are empty")
        
        
    def delete(self, data):
        result = self.database.animals.delete_one(data)
        
        if data:
            # If delete target is found, prints raw JSON output
            # Otherwise, error occurs
            if result.deleted_count > 0:
                return result.raw_result
            else:
                raise Exception("Document with specified key/value pair not in database")     
        else:
            raise Exception("Nothing to delete because data parameter is empty")

