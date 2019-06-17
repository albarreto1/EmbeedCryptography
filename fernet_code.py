from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import statistics as s
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

	print ("Key: \n"+binascii.hexlify(bytearray(key)).decode('ascii')+'\n')

	cipher_suite = Fernet(key)
	cipher_text = cipher_suite.encrypt(message)

	print ("Cipher: \n"+binascii.hexlify(bytearray(cipher_text)).decode('ascii')+'\n')
	plain_text = cipher_suite.decrypt(cipher_text)

	exec_time = time.time() - start_time

	print ("Plain text: \n"+plain_text.decode('ascii')+'\n')

	return exec_time

def doFernet(arch = 'msg2.txt'):

	FILE = open(arch, "r")
	message = FILE.readlines()
	FILE.close()
	total = []
	buffer = []
	for line in message:
		buffer = buffer + [line]
	while (len(total) < 30):
		t = fernet_code(message = line.encode())
		total.append(t)
	return s.mean(total)

def fernet_main():
	msg = ['msg1.txt', 'msg2.txt', 'msg3.txt', 'msg4.txt','msg5.txt']
	mtime = []
	for m in msg:
		mtime.append(doFernet(m))
	FILE = open('fernet_results.txt', 'a')
	FILE.write('Message 1\tMessage 2\tMessage 3\tMessage 4\tMessage 5\n')
	FILE.write('%f\t%f\t%f\t%f\t%f\n'%(mtime[0], mtime[1], mtime[2], mtime[3], mtime[4]))
	FILE.close()

fernet_main()