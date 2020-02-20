import socket
#d = "172.25.11.38"
d = "192.168.0.10"
hostMACAddress = 'B8:27:EB:6F:41:79'
print("check1")
port = 3
print ("ckeck2")
backlog = 1
print ("check3")
size = 1024
print ("check4")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("check5")
s.bind((d,50001))
print ("check6")
s.listen(backlog)
print("check7")
try:
	client, address = s.accept()
	print("check8")
	while 1:
		data = client.recv(size)
		print("check9")
		if data:
			print (data)
			print("check10")
			client.send(data)
except:
	print("cerrando")
	client.close()
	s.close()
