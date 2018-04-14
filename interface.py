#!/usr/bin/python

from getpass import getpass
import random
import sys
# from Crypto.Cipher import AES
# import base64

from pyperclip import copy

# from pandas import DataFrame

from src.crypter import *

from src.database import dbs

class Users:
	"""docstring for Users"""
	def __init__(self):
		self.username = None
		self.password = None

	def take_credentials(self):
		flag = False
		while not flag:
			self.username = raw_input("Enter username : ")
			flag = not dbs.checkUser(self)
			if not flag:
				print "username already exists. Enter again"
		

		temp1 = getpass("Enter New password : ")
		temp2 = getpass("Renter New password : ")
		if temp2 <> temp1:
			sys.exit("Entered password does not match.")
		self.password = temp1
		self.password = setPasswordUsingAES(self.password)
		dbs.storeUsers(self)
		dbs.createUserTable(self)
	def login(self):
		self.username = raw_input("Enter username : ")
		self.password = getpass("Enter password : ")
		if setPasswordUsingAES(self.password) == authenticateUser(self.username): # user has entered the pwd
			# login successful
			return True
		else :
			return False



from src.utils import *
def promp_init():
	print "1. Sign up"
	print "2. Login"

class dbEntry():
	def __init__(self,owner,master_pass):
		self.owner = owner
		self.website = None
		self.username = None
		self.password = None
		self.master_pass = master_pass

	def prompt_UI(self):
		print "1. Save a Password."
		print "2. Copy a saved password"
		print "3. Check Database"
		print "4. Exit"

	def print_entry(self):
		print "Website description : %s " % self.website
		print "Username : %s" % self.username
		print "Password : %s" % self.password


	def take_input(self):
		print "Website description: "
		self.website = raw_input(">")
		print "Username: "
		self.username = raw_input(">")
		self.password = setPasswordUsingAES(getpass("Password: "),self.master_pass)
		# if self.master_pass == None:
		# 	self.master_pass = getpass("Master Password : > ")
		# 	if setPasswordUsingAES(self.master_pass) == getMasterPassword():
		# 	else:
		# 		print "Master Password Incorrect"
		# 		quit()
		dbs.storeEntry(self)
		# print "Password : "
		# self.password = raw_input(">")

	def get_search_entry(self):
		print "Search Password using: "
		print "1. Website"
		print "2. Username"

		response = getint("Select option: ")
		
		if(response == 1):
			ref_string = raw_input("Search Website Query: ")
			out = dbs.getEntry(self.owner,"website",ref_string)
			i=1
			for r in out:
				print i,"|",r[0],"|",r[1],"|",r[2]
				i=i+1
			entry_no = getint("Select Password: ")
			self.get_decrypted_password(out[entry_no-1][3])

		elif(response == 2):
			ref_string = raw_input("Search username Query: ")
			out = dbs.getEntry(self.owner,"username",ref_string)
			i=1
			for r in out:
				print i,"|",r[0],"|",r[1],"|",r[2]
				i=i+1
			entry_no = getint("Select Password: ")
			self.get_decrypted_password(out[entry_no-1][3])
		else:
			print "Enter valid Input Number"


	def get_decrypted_password(self,req_password):
		# if(self.master_pass == None):
		# 	temp_master_pass = getpass("Master Password: > ")
		# 	if setPasswordUsingAES(temp_master_pass) == getMasterPassword():
		# 		self.master_pass = temp_master_pass
		# 	else:
		# 		print "Incorrect Master Password"
		# 		quit()
		passw = getPasswordUsingAES(req_password,self.master_pass)
		idx = passw.find('\x04')
		passw = passw[:idx]
		copy(passw)
		print "Password Copied in Clipboard ! "
		return passw

	def get_complete_info(self):
		out = dbs.getCompleteInfo(self.owner)
		# DataFrame(out,columns=['S.No.','username','website'])
		i=1
		for r in out:
			print i,r[0],r[1]
			i=i+1

if __name__ == '__main__':
	# entry = dbEntry()
	# entry.prompt_UI()
	promp_init()
	response = getint("Select option: ")


	if(response == 1):
		user = Users()
		user.take_credentials()
	if(response == 2):
		user = Users()
		if user.login():
			# user has logged in
			entry = dbEntry(user.username,user.password)
			while True:
				entry.prompt_UI()
				response = getint("Select option: ")
				if(response == 1):
					entry.take_input()
					entry.print_entry()
				elif(response == 2):
					entry.get_search_entry()
				elif(response ==3):
					entry.get_complete_info()
				elif(response == 4):
					quit()
				else:
					print "Enter valid number"

