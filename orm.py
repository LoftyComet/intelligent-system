
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
from sqlalchemy.types import Float
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
    __tablename__ = 'car'
    id = Column(Integer, primary_key=True, autoincrement=True)
    light=Column(Integer,unique=False)
    traffic=Column(Integer, unique=False)
    time = Column(Text(255), unique=False)

    def __repr__(self):
        return "<{} {} >".format(
            self.__class__.__name__,
            self.light,
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


# 路口（id，topRight，eastLeft，eastRight，topLeft）
class Crossing(Base):
    __tablename__ = 'crossing'
    cId=Column(Integer,primary_key=True,unique=False)
    topRight=Column(Integer,unique=False)
    eastLeft=Column(Integer, unique=False)
    eastRight = Column(Integer, unique=False)
    topLeft = Column(Integer, unique=False)

    def __repr__(self):
        return "<{} {} >".format(
            self.__class__.__name__,
            self.id,
        )

    @classmethod
    def find(cls, db, cId):
        """Find a role by name.
        Returns None if not found.
        """
        return db.query(cls).filter(cls.cId == cId).first()

    @classmethod
    def findById(cls, db, id):
        """Find a user by name.
        Returns None if not found.
        """
        return db.query(cls).filter(cls.id == id).first()

# 路口对应信号灯（路口id，信号灯id，对应方位）
class CLight(Base):
    __tablename__ = 'clight'
    cId=Column(Integer,primary_key=True,unique=False)
    light=Column(Integer,primary_key=True,unique=False)
    direction=Column(Text(255), unique=False)

    def __repr__(self):
        return "<{} {} >".format(
            self.__class__.__name__,
            self.cid,
        )

    @classmethod
    def findbyLight(cls, db, light):
        return db.query(cls).filter(cls.light == light).first()

# 可信度知识
class CKnowledge(Base):
    __tablename__ = 'cknowledge'
    id = Column(Integer, primary_key=True, autoincrement=True)
    condition = Column(Text(255), unique=False)
    conclusion = Column(Text(255), unique=False)
    threshold=Column(Float, unique=False)    # 知识使用的阈值
    def __repr__(self):
        return "<{} {} >".format(
            self.__class__.__name__,
            self.id,
        )
    @classmethod
    def findbyId(cls, db, id):
        return db.query(cls).filter(cls.id == id).first()
    @classmethod
    def findbyCondition(cls, db, condition):
        return db.query(cls).filter(cls.condition == condition).all()

# 模糊知识
class FKnowledge(Base):
    __tablename__ = 'fknowledge'
    id = Column(Integer, primary_key=True, autoincrement=True)
    condition = Column(Text(255), unique=False)
    conclusion = Column(Text(255), unique=False)
    threshold=Column(Float, unique=False)    # 知识使用的阈值
    updater=Column(Text(255), unique=False)     # 更新者
    updateTime=Column(Text(255), unique=False)   # 更新时间

    def __repr__(self):
        return "<{} {} >".format(
            self.__class__.__name__,
            self.id,
        )
    @classmethod
    def findbyId(cls, db, id):
        return db.query(cls).filter(cls.id == id).first()
    @classmethod
    def findbyCondition(cls, db, condition):
        return db.query(cls).filter(cls.condition == condition).all()




