#!/usr/bin/env python
#utilisation de python 2.7	

import datetime
import os
import sys
# Ecriture des logs
# date et isActive
date = datetime.datetime.now()
fileActive = open("C:\Users\Acidix\Desktop\isActive.txt", "r")
isActive = fileActive.readlines()
fileActive.close()
file = open("C:\Users\Acidix\Desktop\MainAppLog.txt", "a")
file.write("Starting at: %s \n" % date )
file.write("Is active : %s \n" % isActive )
file.close()

while 1:
	#lancement script srv
	execfile("srv.py")
	#fin du script il a recu une modification 0 ou 1
	date = datetime.datetime.now()
	file = open("C:\Users\Acidix\Desktop\MainAppLog.txt", "a")
	#date de modification
	file.write("Modification Alarm state save at: %s \n" % date )
	fileActive = open("C:\Users\Acidix\Desktop\isActive.txt", "r")
	isActive = fileActive.readlines()
	#ecriture de la nouvelle valeur
	file.write("%s \n" % isActive )
	fileActive.close()
	file.close()
