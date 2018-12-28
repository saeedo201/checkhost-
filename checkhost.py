#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import os
import sys
import socket
import time
import random
if sys.version == "2.7" or "2" :
	pass
elif "3" in sys.version :
	print ("[!] please enter python2 free.py ")
	sys.exit()
os.system('clear')
try :
	print ('''\033[1;31m
               ##################################################
                           _____                                #
                         _/ ____\______   ____   ____           #
                          \   __\\_  __ \_/ __ \_/ __ \          #
                          |  |   |  | \/\  ___/\  ___/          #
                          |__|   |__|    \___  >\___  >         #
                                             \/     \/          #
                                   CODED BY :                   #
                                   Saeed Ahmed                  #
                                   My account:@Zoalktoom             ####################################################
\033[1;m''')
except :
	print ("[!] please enter python2 free.py ")
os.system('printf "\e[1;34m"')
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.3)
os.system('printf "\e[1;31m"')
mengetik('                                  VERSION 1.0                ')
os.system('printf "\e[1;31m"')
mengetik('payload')
mengetik('-------')
os.system('printf "\e[1;34m"')
mengetik('   [1] Creat a payload ')
os.system('printf "\e[1;31m"')
mengetik('host')
mengetik('-------')
os.system('printf "\e[1;34m"')
mengetik("   [2] Brute force for one host ")
mengetik("   [3] Brute force for host list ")
os.system('printf "\e[1;31m"')
mengetik("proxy")
mengetik("-------")
os.system('printf "\e[1;34m"')
mengetik("   [4] ")
os.system('printf "\e[1;31m"')
mengetik("ssh account")
mengetik("-----------")
os.system('printf "\e[1;34m"')
mengetik("   [5] Creat ssh account ")
os.system('printf "\e[1;31m"')
choose =raw_input("[Chose Number]~#:")
if choose == '1':
	os.system('printf "\e[1;33m"')
	mengetik('payload')
	os.system('clear')
	os.system('printf "\e[1;31m"')
	os.system('toilet payload')
	payload =raw_input("Inter your free host (without http or https) ==> ")
	print('your payload : CONNECT [host_port] HTTP/1.1[crlf][crlf]POST http://{} [protocol][crlf]Host: {}[crlf]Connection: Keep-Alive[crlf]Referer: {}[crlf][crlf]'.format (payload,payload,payload))
elif choose == '2':
	os.system('printf "\e[1;33m"')
	mengetik('host')
	os.system('clear')
	os.system('printf "\e[1;31m"')
	os.system('toilet ONE HOST')
	host=raw_input("Inter your host : ")
	try :
		request = b"GET / HTTP/1.1\nHost: {}\n\n".format(host)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(("{}".format(host), 80))
		s.send(request)
		result = s.recv(1000)
		while (len(result) > 0):
			if result==b'HTTP/1.1 200 OK\r':
				print ("Success !")
				result = s.recv(1000)
                                break;
	except socket.error :
		print("false")

elif choose == '3':
	os.system('printf "\e[1;33m"')
	mengetik('host')
	os.system('clear')
	os.system('printf "\e[1;31m"')
	os.system('toilet HOST LIST')
	hostlist=raw_input("Inter your list : ")
	i = open("{}".format(hostlist), "r")
	o = i.readlines()
	for host in o:
		sys.stdout.write("\r[*] Trying ..... {}\n".format(host))
		sys.stdout.flush()
        try :
         	request = b"GET / HTTP/1.1\nHost: {}\n\n".format(host)
         	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         	s.connect(("{}".format(host), 80))
         	s.send(request)
         	result = s.recv(1000)
         	while (len(result) > 0):
         		if result==b'HTTP/1.1 200 OK\r':
         			print ("Success !")
         			result = s.recv(1000)
         			break;
        except socket.error :
        	print("false")
elif choose == '5' :
	print ("   [1] fastssh")
	website =input("select the website : ")
	if website == 1 :
		continent=input("select the continent (Asia , Europe , North America , South America , Africa , Ocrania ) : ")
                print ('Your account: ........')
