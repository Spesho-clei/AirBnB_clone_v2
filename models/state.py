#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
import env

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    __cities = relationship('City', backref='state', cascade='all, delete')

    @property
    def cities(self):
        """
        get all cities with the current state id
        """
        from models import storage
        if not env.DBTYPE:
            return [
                v for k, v in storage.all(City).items()
                if v.state_id == self.id
            ]
        return self.__cities
    
