#!/usr/bin/python

#!/usr/bin/python

#----------------------------------------------------------------------------------------------------------------------#
# References:                                                                                                          #
# - https://pythonspot.com/en/orm-with-sqlalchemy/                                                                     #
#----------------------------------------------------------------------------------------------------------------------#

from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

# - Engine Configuration
#   http://docs.sqlalchemy.org/en/latest/core/engines.html
#  default mysql
engine = create_engine('mysql://root:kaned2345@localhost/testdb', echo=True)
#   -requires install 'MySQLdb' -> $ sudo apt-get install python-mysqldb
#   -database must previously exists
Base = declarative_base()


#----------------------------------------------------------------------------------------------------------------------#
class Student(Base):
    """"""
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    username = Column(String,10)
    firstname = Column(String,10)
    lastname = Column(String,10)
    university = Column(String,10)

    # ----------------------------------------------------------------------
    def __init__(self, username, firstname, lastname, university):
        """"""
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.university = university


# create tables
Base.metadata.create_all(engine)



