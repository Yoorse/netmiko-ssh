from connect import *
from netmiko import ConnectHandler
import sys


command = "show run"

net_connect = ConnectHandler(**cisco)

output = net_connect.send_command(command)


with open('running_config.txt', 'w') as f:
	
	print(output, file=f)
	
net_connect.disconnect()

