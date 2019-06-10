import binascii
import time


def rsa_code(message = 'Rosetta Code!'):

	n = 9516311845790656153499716760847001433441357    # p*q = modulus
	e = 65537
	d = 5617843187844953170308463622230283376298685

	start_time = time.time()

	print('message                 ', message)

	hex_data   = binascii.hexlify(message.encode())
	print('hex data                ', hex_data)
	 
	plain_text = int(hex_data, 16)
	print('plain text integer      ', plain_text)
	 
	if (plain_text > n):
	  raise Exception('plain text too large for key')
	 
	encrypted_text = pow(plain_text,     e, n)
	print('encrypted text integer  ', encrypted_text)
	 
	decrypted_text = pow(encrypted_text, d, n)
	print('decrypted text integer  ', decrypted_text)

	exec_time = time.time() - start_time

	print('message                 ', binascii.unhexlify(hex(decrypted_text)[2:]).decode())     # [2:] slicing, to strip the 0x part 

	return exec_time