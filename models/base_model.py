#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
<<<<<<< HEAD


class BaseModel:
    """A base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
=======
from uuid import uuid4
import models

class BaseModel:
""" construct """

def __init__(self, *args, **kwargs):
""" Construct """

if kwargs:
    for key, value in kwargs.items():
        if key == '__class__':
            continue
        elif key == 'updated_at':
            value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
        elif key == 'created_at':
            value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            def __str__(self):
                """ String """
                return('[' + self.__class__.__name__ + '] (' + self.id +
                        ') ' + str(self.__dict__))

            def save(self):
                """ save function """
                self.updated_at = datetime.now()
                models.storage.save()


            def to_dict(self):
                """ Return a dictonary """
                aux_dict = self.__dict__.copy()
                aux_dict['__class__'] = self.__class__.__name__
                aux_dict['created_at'] = self.created_at.isoformat()
                aux_dict['updated_at'] = self.updated_at.isoformat()

            return aux_dict
>>>>>>> 73a076deabdb66313857081f333973f27192cb3f
