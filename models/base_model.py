#!/usr/bin/python3
''' Console module '''

from datetime import datetime
import uuid


class BaseModel:
    ''' The BaseModel class, the parent class of all other classes '''

    def __init__(self):
        ''' Initializer method '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        ''' updates `updated_at` with the current time '''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' returns a dictionary containing all keys/values
            of __dict__ of the instance
        '''
        d = self.__dict__
        d['__class__'] = self.__class__.__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        return d

    def __str__(self):
        ''' Returns a string representation of a BaseModel object '''
        return ("[" + self.__class__.__name__ + "]" + " (" + self.id + ") "
                + str(self.__dict__))
