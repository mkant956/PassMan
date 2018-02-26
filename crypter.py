#!/usr/bin/python

import random
import string

from Crypto.Cipher import AES
import base64

from database import dbs
# import database as database
pad_char = '\x04'
def getMasterPassword():
	# get master password from database
	master_pass = dbs.getMasterPassword()
	return master_pass
	# return "LV6uS0LrLaK9wWqrFEPTNg=="

def getSecretKey(size = 16):
	chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
	key = ''.join([random.choice(chars) for x in range(size)])
	return key

def fixLength(c,input_text):
	if(len(input_text) % 16 == 0):
		return input_text
	original_size = len(input_text)
	final_size = (original_size/16 + 1)*16
	return input_text + c*(final_size - original_size)


def setPasswordUsingAES(raw_password,secret_key = '_master_password'):

	# secret_key = getSecretKey(16)
	raw_password = fixLength(pad_char,raw_password)
	if(len(secret_key) % 16 <> 0):
		secret_key = fixLength(pad_char,secret_key)
	cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
	encoded = base64.b64encode(cipher.encrypt(raw_password))

	# print encoded
	return encoded

def getPasswordUsingAES(hash_msg,secret_key):
	if(len(secret_key) % 16 <> 0):
		secret_key = fixLength(pad_char,secret_key)
	cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
	decoded = cipher.decrypt(base64.b64decode(hash_msg))

	return decoded

	# print decoded


if __name__ == '__main__':
	getMasterPassword()
	# quit()
	key = getSecretKey()
	master_pass = "mp"
	enc = setPasswordUsingAES(master_pass)
	print enc
	dec = getPasswordUsingAES(enc,"_master_password")
	print enc
	print dec