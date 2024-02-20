#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    
    storage_type = os.getenv('HBNB_TYPE_STORAGE')

    if storage_type == 'db':
        place_id = Column(String(60), nullable=False, ForeignKey="places.id")
        user_id = Column(String(60), nullable=False, ForeignKey="users.id")
        text = Column(String(1024), nullable=False)
    else:
        place_id = ""
        user_id = ""
        text = ""
