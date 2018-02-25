#!/usr/bin/python

import random
import string

from Crypto.Cipher import AES
import base64

def getMasterPassword():
	# get master password from database
	return "LV6uS0LrLaK9wWqrFEPTNg=="

def getSecretKey(size = 16):
	chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
	key = ''.join([random.choice(chars) for x in range(size)])
	return key

def fixLength(c,raw_password):
	original_size = len(raw_password)
	final_size = (original_size/16 + 1)*16
	return raw_password + c*(final_size - original_size)


def setPasswordUsingAES(raw_password,secret_key = '_master_password'):

	# password = None
	# msg_text = raw_password
	# secret_key = b'aaaaaaaabbbbbbbb'
	# cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
	# encoded = base64.b64encode(cipher.encrypt(msg_text))
	# print encoded
	# decoded = cipher.decrypt(base64.b64decode(encoded))
	# print decoded

	# secret_key = getSecretKey(16)
	if(len(raw_password) % 16 <> 0):
		raw_password = fixLength('$',raw_password)
	cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
	encoded = base64.b64encode(cipher.encrypt(raw_password))

	# print encoded
	return encoded

def getPasswordUsingAES(hash_msg,secret_key):
	cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
	decoded = cipher.decrypt(base64.b64decode(hash_msg))

	return decoded

	# print decoded


if __name__ == '__main__':
	key = getSecretKey()
	enc = setPasswordUsingAES("masterpassword")
	print enc
	quit()
	dec = getPasswordUsingAES(enc,key)
	print enc
	print dec