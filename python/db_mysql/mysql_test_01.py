#!/usr/bin/python

# Install MySQLdb
# - Ubuntu 14
# $ sudo apt-get install mysqldb

import MySQLdb

DBNAME='testdb'
DBUSER='root'
DBPASS='kaned2345'
DBHOST='localhost'

#-----------------------------------------------------------------------------------
# EXAMPLE 001 - Execute simple query
#-----------------------------------------------------------------------------------

# Open database connection
db = MySQLdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)
# prepare a cursor objecto using cursor() method
cursor = db.cursor()
# execute SQL query using execute() method
cursor.execute("SELECT VERSION()")
# fetch a single row using fetchone() method
data = cursor.fetchone()
print "Database version : %s" % data
# disconnect from server
db.close()

#-----------------------------------------------------------------------------------
# EXAMPLE 002 - Create Database Table
#-----------------------------------------------------------------------------------

db = MySQLdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql="""CREATE TABLE EMPLOYEE(
       FIRST_NAME CHAR(20) NOT NULL,
       LAST_NAME CHAR(20),
       AGE INT,
       SEX CHAR(1),
       INCOME FLOAT)"""
cursor.execute(sql)
db.close()

#-----------------------------------------------------------------------------------
# EXAMPLE 003 - INSERT Operation
#-----------------------------------------------------------------------------------

db = MySQLdb.connect(DBHOST, DBUSER, DBPASS, DBNAME)
cursor = db.cursor()
sql = """INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
         VALUES              ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback

db.close()