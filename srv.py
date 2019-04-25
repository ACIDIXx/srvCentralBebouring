#!/usr/bin/env python
#utilisation de python 2.7	
import socket

isAlarmEnabled = None
#ip actuelle de l'host
TCP_IP = '10.144.50.66'
TCP_PORT = 5005
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print "Waiting for connection ..."
conn, addr = s.accept()
print "Modification des parametres de l'alarme de", addr
#print 'Connection address:', addr
while 1:
	data = conn.recv(BUFFER_SIZE)
	if not data: break
	print "received data:", data
	if data.find('3')!=-1 :
		file = open("C:\Users\Acidix\Desktop\isActive.txt", "r")
		fileT = open("C:\Users\Acidix\Desktop\MainAppLog.txt", "a") #Log
		fileT.write("ouverture du fichier") #log
		isActive = file.readlines() #pas bon ca parce qu'il fait des truc chelou en lisant 
		fileT.write("fichier lu %s" % isActive) #log
		file.close()
		fileT.close()
		 #if isActive.find('1')!=-1 :
		fileT = open("C:\Users\Acidix\Desktop\MainAppLog.txt", "a") #Log
		fileT.write("lecture 1") #log
		conn.send("31")
		fileT.close()
		#else:
			#fileT = open("C:\Users\Acidix\Desktop\MainAppLog.txt", "a") #Log
			#fileT.write("lecture 0") #log
			#conn.send("30")
			#fileT.close()
	else:
		conn.send(data)
		file = open("C:\Users\Acidix\Desktop\isActive.txt", "w")
		file.writelines(data)
		file.close()
conn.close()

