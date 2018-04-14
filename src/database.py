#!/usr/bin/python
import MySQLdb
 
class database:
	def __init__(self):
		self.db = MySQLdb.connect(host="localhost",  # your host 
                     user="root",       # username
                     passwd="root",     # password
                     db="passman")   # name of the database
 
		# Create a Cursor object to execute queries.
		self.cur = self.db.cursor()

	def storeEntry(self,obj):
		# p = "INSERT INTO %s(username,password,update_date,website) \
		#  VALUES (\"%s\",\"%s\",CURDATE(),\"%s\")" % (obj.owner,obj.username,obj.password,obj.website)
		# # print p
		self.cur.execute("INSERT INTO %s(username,password,update_date,website) \
		 VALUES (\"%s\",\"%s\",CURDATE(),\"%s\")" % (obj.owner,obj.username,obj.password,obj.website))
		self.db.commit()

	def updateEntry(self,obj,userid):
		# p = "INSERT INTO %s(username,password,update_date,website) \
		#  VALUES (\"%s\",\"%s\",CURDATE(),\"%s\")" % (obj.owner,obj.username,obj.password,obj.website)
		# print p
		self.cur.execute("UPDATE %s SET password=\"%s\" WHERE id=%s"%(obj.owner,obj.password,userid))
		self.db.commit()

	def storeUsers(self,obj):
		self.cur.execute("INSERT INTO Users(username,password) \
		 VALUES (\"%s\",\"%s\")" % (obj.username,obj.password))
		self.db.commit()

	def deleteUser(self,obj):
		self.cur.execute("DROP TABLE %s"%obj.owner)
		self.cur.execute("DELETE FROM Users WHERE username = \"%s\""%obj.owner)
		self.db.commit()

	def checkUser(self,obj):
		self.cur.execute("SELECT * FROM Users WHERE username = \"%s\""%obj.username)

		if len(self.cur.fetchall()):
			return True
		else:
			return False

	def createUserTable(self,obj):
		self.cur.execute("create table if not exists %s(id int(11) NOT NULL AUTO_INCREMENT,username varchar(80),password varchar(200),update_date DATE, website varchar(200),PRIMARY KEY(id));" % obj.username)
		self.db.commit()

	def getMasterPassword(self):
		self.cur.execute("SELECT * FROM masterpass")
		for r in self.cur.fetchall():
			return r[0]

	def getUserPassword(self,username):
		self.cur.execute("SELECT * FROM Users WHERE username = \"%s\""%username)
		for r in self.cur.fetchall():
			return r[2]

	def getEntry(self,owner,col_name,ref_string):
		self.cur.execute("SELECT username,website,update_date,password,id FROM %s WHERE %s LIKE \""%(owner,col_name)+"%"+"%s"%ref_string+"%"+"\"")
		return self.cur.fetchall()
		# for r in self.cur.fetchall():
			# return r[0],r[1],r[2]

	def getCompleteInfo(self,owner):
		self.cur.execute("SELECT username,website FROM %s"%owner)
		return self.cur.fetchall()

	def __del__(self):
		self.db.close()

	def tempFuncEntry(self):
		self.cur.execute("INSERT INTO user_pass(username,password,update_date,website) VALUES (\"user1\",\"password1foruser1\",CURDATE(),\"h\") ")
		self.db.commit()

dbs = database()

# # Select data from table using SQL query.
# cur.execute("INSERT INTO user_pass(id,username,password,update_date,website) VALUES (1,\"user1\",\"password1foruser1\",CURDATE()),\"hello\" ")
# cur.execute("SELECT * FROM user_pass")
 
# db.commit()
# # print the first and second columns      
# for row in cur.fetchall() :
#     print row[0], " ", row[1], " ", row[2], " ", row[3]
# print getMasterPassword()
# db.close()
if __name__ == '__main__':
	# dbs.tempFuncEntry()
	out = dbs.getEntry("username","mkan")
	print out
	# print username,"|",website,"|",update_date