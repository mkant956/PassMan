#!/usr/bin/python

from getpass import getpass
import random

from Crypto.Cipher import AES
import base64

from crypter import *

class dbEntry():
	def __init__(self):
		self.website = None
		self.username = None
		self.password = None
	def print_entry(self):
		print "Website description : %s " % self.website
		print "Username : %s" % self.username
		print "Password : %s" % self.password
	def take_input(self):
		print "Website description: "
		self.website = raw_input(">")
		print "Username: "
		self.username = raw_input(">")
		master_pass = getpass("Master Password : > ")
		if setPasswordUsingAES(master_pass) == getMasterPassword():
			self.password = setPasswordUsingAES(getpass())
		else:
			print "Master Password Incorrect"
			quit()
		# print "Password : "
		# self.password = raw_input(">")

	


if __name__ == '__main__':
	entry = dbEntry()
	entry.take_input()
	entry.print_entry()