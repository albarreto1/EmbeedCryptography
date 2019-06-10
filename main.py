from rsa_code import *
from isaac_code import *
from fernet_code import *

rsa = rsa_code('analise')

fernet = fernet_code(message = 'analise de desempenho'.encode())

fernet2 = fernet_code(password = 'projeto final'.encode(), message = 'analise de desempenho'.encode())

isaac = isaac_code(message = 'analise de desempenho', key = 'projeto final')

print(rsa, fernet, fernet2, isaac)