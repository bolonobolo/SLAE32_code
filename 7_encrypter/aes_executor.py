#!/usr/bin/python

# AES Block Cipher script for shellcodes
# Author: @bolonobolo
# Date: 2019/10/18

from Crypto.Cipher import AES
from base64 import b64encode,b64decode
import random
import string
import os

def getMode():
	while True:
		print ("Welcome to AES Block Cipher script for shellcodes")
		print("Do you wish do (e)ncrypt, (d)ecrypt or e(x)ecute?")
		mode = raw_input().lower()
		if mode in "encrypt e decrypt d execute x".split():
			return mode
		else:
			print('Enter either "encrypt" or "e", "decrypt" or "d", "execute" or "x".')

def getMessage():
	print("Enter the text")
	return raw_input()

def getKey():
	print("Enter the key")
	return raw_input()

def getIV():
	# 16 byte iv
	iv = "0123456789abcdef"
	return iv


def genkey(length):
	key = []
	# in ascii one letter = 8 bit = 1 byte 
	# AES needs 128, 192, or 256 bits, i choosed 256 256/8 = 32
	for _ in range (0,length):
		key.append(random.SystemRandom().choice(
				string.ascii_uppercase + string.ascii_lowercase + string.digits
				)) 
	return ''.join(key)

def aes(cipher, key, iv):
	cipher = AES.new(key, AES.MODE_CBC, iv)
	return cipher

def padding(size, text):
	while len(text) % size != 0:
			text += " "
	return text	

def cipherAlgo(key, text, size, iv):
	cipher = aes("aes", key, iv)	
	text = padding(size, text)
	text = cipher.encrypt(text)
	msg = b64encode(text)
	return msg

def decipherAlgo(key, text, iv):
	cipher = aes("aes", key, iv)
	text = b64decode(text)	
	msg = cipher.decrypt(text)
	return msg

def executeAlgo(code):
	code = code.replace(" ", "") # eventualy clean code from blank spaces
	file = open("shellcode.c", "w")
	file.write('''
		#include<stdio.h>
		#include<string.h>

		unsigned char code[] = \"''' + code + '''";

		void main() {

			printf(\"Shellcode Length:  %d\\n\", strlen(code));

			int (*ret)() = (int(*)())code;

			ret();

		}'''
	)
	file.close()
	os.system("gcc -fno-stack-protector -z execstack -m32 shellcode.c -o shellcode 2>/dev/null && ./shellcode")

def main():
	mode = getMode()
	text = getMessage()
	iv = getIV()
	if mode[0] == "e":
		key = genkey(32) # 256 bits of key
		size = 16 # block size has to be 16 bytes
		msg = cipherAlgo(key, text, size, iv)
		print("Encrypted shellcode: %s" % (msg))
		print("The key is: %s" % (key))
		# print("The IV is: %s" % (iv))
	elif mode[0] == "d":
		key = getKey()
		msg = decipherAlgo(key, text, iv)
		print("Decrypted shellcode: %s" % (msg))
	elif mode[0] == "x":
		key = getKey()
		msg = decipherAlgo(key, text, iv)
		print("Decrypted shellcode: %s" % (msg))
		executeAlgo(msg)	

if __name__ == '__main__':
	main()
