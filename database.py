#!/usr/bin/python
import MySQLdb
 
db = MySQLdb.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="root",     # password
                     db="passman")   # name of the database
 
# Create a Cursor object to execute queries.
cur = db.cursor()
 
# Select data from table using SQL query.
cur.execute("INSERT INTO user_pass(id,username,password,update_date,website) VALUES (1,\"user1\",\"password1foruser1\",CURDATE()),\"hello\" ")
cur.execute("SELECT * FROM user_pass")
 
db.commit()
# print the first and second columns      
for row in cur.fetchall() :
    print row[0], " ", row[1], " ", row[2], " ", row[3]

db.close()