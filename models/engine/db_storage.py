#!/usr/bin/python3
"""import modules"""

from models.amenity import Amenity
from models.base_model import Base
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from models.user import User

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
import os

classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """new class"""
    __engine = None
    __session = None

    def __init__(self):
        """init function"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB'),
            pool_pre_ping=True))

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """all function"""
        new_dict = {}
        for clas in classes:
            if cls is None or cls is classes[clas] or cls is clas:
                objs = self.__session.query(classes[clas]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict


    def new(self, obj):
        """new obj"""
        self.__session.add(obj)

    def save(self):
        """to save"""
        self.__session.commit()

    def delete(self, obj=None):
        """to delete"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """to reload"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(
            bind=self.__engine,
            expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """ call remove method on
            the private session
        """
        self.__session.close()
