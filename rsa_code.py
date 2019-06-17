import binascii
import time
from Crypto.PublicKey import RSA

def rsa_code(message = 'Analise de desempe'):

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



def rsa_code2(key_size = 2048, message = 'mensagem limpa'):
    start_time = time.time()

    key = RSA.generate(key_size)
    #private_key = key.exportKey()
    #print(private_key)
    #file_out = open("private.pem", "wb")
    #file_out.write(private_key)
    #public_key = key.publickey().exportKey()
    #print(public_key)
    #file_out = open("receiver.pem", "wb")
    #file_out.write(public_key)

    hex_data   = binascii.hexlify(message.encode())

    plain_text = int(hex_data, 16)
    print('plain text integer      ', plain_text)

    enc = key.encrypt(plain_text, 123456)
    dec = key.decrypt(enc)

    exec_time = time.time() - start_time

    print('message                 ', binascii.unhexlify(hex(dec)[2:]).decode())     # [2:] slicing, to strip the 0x part 

    return exec_time

