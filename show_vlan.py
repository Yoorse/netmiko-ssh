from connect import *
from netmiko import ConnectHandler
import sys


command = "show vlan br"

net_connect = ConnectHandler(**cisco)

output = net_connect.send_command(command)

print(output)

original_stdout = sys.stdout

with open('vlans.txt', 'w') as f:
	sys.stdout = f
	
	print(output)
	sys.stdout = original_stdout 
