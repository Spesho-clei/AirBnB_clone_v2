#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime

from sqlalchemy import DATETIME, Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60),
                nullable=False,
                primary_key=True,
                unique=True)
    created_at = Column(DATETIME,
                        nullable=False,
                        default=datetime.utcnow())
    updated_at = Column(DATETIME,
                        nullable=False,
                        default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            for k in kwargs:
                if k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.fromisoformat(kwargs[k]))
                elif k != '__class__':
                    setattr(self, k, kwargs[k])
        if self.id is None or self.id == '':
            self.id = str(uuid.uuid4())
        d = datetime.now()
        if self.created_at is None:
            self.created_at = self.updated_at = d
        if self.updated_at is None:
            self.updated_at = d

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        for i in dictionary:
            if type(dictionary[i]) is datetime:
                dictionary[i] = dictionary[i].isoformat()
        if '_sa_instance_state' in dictionary.keys():
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        '''deletes the current instance from the storage'''
        from models import storage
        storage.delete(self)        

