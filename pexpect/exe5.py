#!/usr/bin/env python
# for SSH create user with privilage level 15 
import getpass
from pexpect import pxssh

devices = {'CoreSW': {'prompt': 'CoreSW#', 'ip': '192.168.100.20'}, 
           'SW1': {'prompt': 'SW1#', 'ip': '192.168.100.21'}}
commands = ['term length 0', 'show version', 'show run']

username = input('Username: ')
password = getpass.getpass('Password: ')

# Starts the loop for devices
for device in devices.keys(): 
    outputFileName = device + '_output.txt'
    device_prompt = devices[device]['prompt']

    child = pxssh.pxssh()
    child.login(devices[device]['ip'], username.strip(), password.strip(), auto_prompt_reset=False)
    
    # Starts the loop for commands and write to output
    with open(outputFileName, 'wb') as f:
        for command in commands:
            child.sendline(command)
            child.expect(device_prompt)
            f.write(child.before)
    
    child.logout()
