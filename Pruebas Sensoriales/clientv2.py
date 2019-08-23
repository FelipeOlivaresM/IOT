#  Script para cliente usando la version 3.2 de python
# Libreria

#d="172.25.11.38"

d="192.168.0.10"

import socket
import time
import random
serverMACAddress = 'B8:27:EB:6F:41:79' # Dirreccion MAC a la cual se quiere conectar
port = 3
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((d,50001))

while 1:
	text = "temperatura" 
	s.send(text)
	time.sleep(10)
s.close()


