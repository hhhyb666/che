from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash

from extensions import db
import os

from sqlalchemy import create_engine,Column,String,Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

#建立链接
engine=create_engine('sqlite:///' + os.path.join(basedir, 'datatttyy.db'),echo=True)
#建立会话
DBSession = sessionmaker(bind=engine)
session = DBSession()
Base=declarative_base()


def CreatDb():
    Base.metadata.create_all(engine)

def delDb(): #删除表
    Base.metadata.drop_all(engine)



class User(Base):
    __tablename__ ='user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    locale = db.Column(db.String(20))
    items = db.relationship('Item', back_populates='author', cascade='all')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)




#多条件查询，这里注意的是filter_by和filter的区别，filter可以多表查询。比较运算符也不一样。filter必需带表名
#querydt=session.query(Mybase).filter(Mybase.myid == 'asd').filter(Mybase.price == 'bbbb')
#for i in querydt:
#    print(i.myid)
class Item(Base):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', back_populates='items')