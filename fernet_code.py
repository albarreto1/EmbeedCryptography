from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import sys
import binascii
import base64
import time

def gen_key(p):
	digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
	digest.update(p)
	return base64.urlsafe_b64encode(digest.finalize())

def fernet_code(password = '', message = ''):

	start_time = time.time()
	if (len(password)>1):
		key = gen_key(password)
	else:
		key = Fernet.generate_key()

	print ("Key: "+binascii.hexlify(bytearray(key)).decode('ascii'))

	cipher_suite = Fernet(key)
	cipher_text = cipher_suite.encrypt(message)

	print ("Cipher: "+binascii.hexlify(bytearray(cipher_text)).decode('ascii'))
	plain_text = cipher_suite.decrypt(cipher_text)

	exec_time = time.time() - start_time

	print ("Plain text: "+plain_text.decode('ascii'))

	return exec_time