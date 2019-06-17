from rsa_start import rsa_main
from isaac_code import isaac_main
from fernet_code import fernet_main
from CPUusage import cpuusage_main
import threading

t1 = threading.Thread(target=cpuusage_main, args=('CPUUsageRSA.txt'))
t2 = threading.Thread(target=cpuusage_main, args=('CPUUsageFERNET.txt'))
t3 = threading.Thread(target=cpuusage_main, args=('CPUUsageISAAC.txt'))

t1.start()
rsa_main()
t1.cancel()
t2.start()
fernet_main()
t2.cancel()
t3.start()
isaac_main()
t3.cancel()

print('fim do experimento')