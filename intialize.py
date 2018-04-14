#!/usr/bin/python

import MySQLdb

from getpass import getpass

from src.utils import *

from src.crypter import *

# create table if not exists Users(id int(11) NOT NULL AUTO_INCREMENT,username varchar(80),password varchar(200),PRIMARY KEY (id));

# make table for Users

def createTable():
    # db = MySQLdb.connect(host="localhost",  # your host 
    #                  user="root",       # username
    #                  passwd="root",     # password
    #                  db="passman")   # name of the database
 
    # # Create a Cursor object to execute queries.
    # cur = db.cursor()

    # print "Enter root password -"

    cmd = "mysql -u root -p < src/create.sql"
    executeBashCommand(cmd)

    # mp = getpass("Enter Master Password:> ")

    # hashed_mp = setPasswordUsingAES(mp)
    # cur.execute("DELETE FROM masterpass")
    # cur.execute("INSERT INTO masterpass(masterpassword) VALUES (\"%s\")" % hashed_mp)
    # db.commit()


if __name__ == '__main__':
    createTable()