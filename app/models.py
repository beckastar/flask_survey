
from app import db
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, scoped_session


engine = create_engine('sqlite:///bikes.db', convert_unicode=True)

session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = session.query_property()

class User(db.Model):
    __tablename__="user"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(15))
    email = db.Column(db.String(25))
    age= db.Column(db.Integer)

def main():
    Base.metadata.create_all(ENGINE)


if __name__ == "__main__":
    main()
