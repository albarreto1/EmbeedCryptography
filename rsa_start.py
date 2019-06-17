# -*- coding: utf-8 -*-

from rsa_code import rsa_code, rsa_code2
import statistics as s

def doRSA(arch = 'msg2.txt', key_size = 2048):
    #primeiramente, acertar os tamanhos de strings para teste: devido as
    #limitações dessa implementação do RSA, acho que mensagens de 10, 30, 50 e 
    #100 caracteres está aceitável

    #As mensagens serão coletadas de um arquivo de texto
    FILE = open(arch, "r")

    #A implementação do algoritmo escolhida tem uma limitação com relação ao 
    #tamanho da mensagem. O número máximo de caracteres na mensagem é 17. Logo,
    #devem ser passados 17 carcteres por vez, no máximo
    
    support = int(key_size/8)
    
    buffer = []
    message = []
    message = message + FILE.readlines()
    print(message)
    for line in message:
        while(len(line) > support):
            buffer.append(line[:support-1])
            line = line[support:]
        buffer.append(line)
        FILE.close()
    
    total = []
    while (len(total) < 30):
        t = 0
        for b in  buffer:
            t = t + rsa_code2(key_size, b)
        total.append(t)
    return s.mean(total)

def rsa_main():
    msg = ['msg1.txt', 'msg2.txt', 'msg3.txt', 'msg4.txt']
    mtime = []
    for m in msg:
        mtime.append(doRSA(m))
    FILE = open('rsa_results.txt', 'a')
    FILE.write('Message 1\tMessage 2\tMessage 3\tMessage 4\n')
    FILE.write('%f\t%f\t%f\t%f\n'%(mtime[0], mtime[1], mtime[2], mtime[3]))
    FILE.close()
    
