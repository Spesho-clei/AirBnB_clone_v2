#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import env

from sqlalchemy import Column, Float, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60),
                     ForeignKey('cities.id'),
                     nullable=False)
    user_id = Column(String(60),
                     ForeignKey('users.id'),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    __reviews = relationship("Review", cascade="all, delete", backref="place")
    __amenities = relationship("Amenity", secondary=place_amenity,
                               viewonly=False)
    amenity_ids = []

    @property
    def reviews(self):
        """getter attribute returns the list of Review instances"""
        if env.HBNB_TYPE_STORAGE == 'db':
            return self.__reviews

        from models import storage
        from models.review import Review
        review_list = []
        for review in storage.all(Review).values():
            if review.place_id == self.id:
                review_list.append(review)
        return review_list

    @property
    def amenities(self):
        """getter attribute returns the list of Amenity instances"""
        if env.HBNB_TYPE_STORAGE == 'db':
            return self.__amenities

        from models import storage
        from models.amenity import Amenity
        amenity_list = []
        for amenity in storage.all(Amenity).values():
            if amenity.place_id in self.amenity_ids:
                amenity_list.append(amenity)
        return amenity_list
