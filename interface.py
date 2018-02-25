#!/usr/bin/python

from getpass import getpass
import random

from Crypto.Cipher import AES
import base64

from pyperclip import copy

from crypter import *

class dbEntry():
	def __init__(self):
		self.website = None
		self.username = None
		self.password = None
		self.master_pass = None
	def print_entry(self):
		print "Website description : %s " % self.website
		print "Username : %s" % self.username
		print "Password : %s" % self.password


	def take_input(self):
		print "Website description: "
		self.website = raw_input(">")
		print "Username: "
		self.username = raw_input(">")
		self.master_pass = getpass("Master Password : > ")
		if setPasswordUsingAES(self.master_pass) == getMasterPassword():
			self.password = setPasswordUsingAES(getpass(),self.master_pass)
		else:
			print "Master Password Incorrect"
			quit()
		# print "Password : "
		# self.password = raw_input(">")


	def get_decrypted_password(self):
		if(self.master_pass == None):
			self.master_pass = getpass("Master Password : > ")
		passw = getPasswordUsingAES(self.password,self.master_pass)
		idx = passw.find('\x04')
		passw = passw[:idx]
		copy(passw)
		return passw


if __name__ == '__main__':
	entry = dbEntry()
	entry.take_input()
	entry.print_entry()
	entry.get_decrypted_password()