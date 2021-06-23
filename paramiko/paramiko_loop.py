import paramiko
import time

ip = '192.168.100.20'
username = 'admin'
password = 'cisco'

a = int (input('Enter first loopback in range : '))
b = int (input('Enter last loopback in range : ')) + 1

SESSION = paramiko.SSHClient()
SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
SESSION.connect(ip,port=22,
                username=username,
                password=password,
                look_for_keys=False,
                allow_agent=False)

DEVICE_ACCESS = SESSION.invoke_shell()
DEVICE_ACCESS.send(b'config t\n')

for N in range (a,b):
    DEVICE_ACCESS.send('int lo ' + str(N) + '\n')
    DEVICE_ACCESS.send('ip address 1.1.1.' + str(N) + ' 255.255.255.255' + '\n')  

time.sleep(3)
DEVICE_ACCESS.send(b'do term length 0\n')
DEVICE_ACCESS.send(b'do show ip int brief\n')
time.sleep(3)
output = DEVICE_ACCESS.recv(65000)
print (output.decode('ascii'))

SESSION.close()