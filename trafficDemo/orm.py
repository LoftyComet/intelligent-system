
from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import DateTime
from sqlalchemy import event
from sqlalchemy import exc
from sqlalchemy import ForeignKey
from sqlalchemy import inspect
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import or_
from sqlalchemy import select
from sqlalchemy import Table
from sqlalchemy import Unicode
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref
from sqlalchemy.orm import interfaces
from sqlalchemy.orm import object_session
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from sqlalchemy.sql.expression import bindparam
from sqlalchemy.types import LargeBinary
from sqlalchemy.types import Text
from sqlalchemy.types import TypeDecorator
from tornado.log import app_log


meta = MetaData(
    naming_convention={
        "ix": "ix_%(column_0_label)s",
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)

Base = declarative_base(metadata=meta)
Base.log = app_log


class User(Base):
    """User Roles"""

    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Unicode(255), unique=True)

    def __repr__(self):
        return "<{} {} >".format(
            self.__class__.__name__,
            self.name,
        )

    @classmethod
    def find(cls, db, name):
        """Find a role by name.
        Returns None if not found.
        """
        return db.query(cls).filter(cls.name == name).first()

    @classmethod
    def findById(cls, db, id):
        """Find a user by name.
        Returns None if not found.
        """
        return db.query(cls).filter(cls.id == id).first()

class Car(Base):
    """User Roles"""

    __tablename__ = 'car'
    id = Column(Integer, primary_key=True, autoincrement=True)
    light=Column(Integer,unique=False)
    traffic=Column(Integer, unique=False)
    time = Column(Text(255), unique=False)

    def __repr__(self):
        return "<{} {} >".format(
            self.__class__.__name__,
            self.name,
        )

    @classmethod
    def find(cls, db, light):
        """Find a role by name.
        Returns None if not found.
        """
        return db.query(cls).filter(cls.light == light).first()

    @classmethod
    def findById(cls, db, id):
        """Find a user by name.
        Returns None if not found.
        """
        return db.query(cls).filter(cls.id == id).first()


