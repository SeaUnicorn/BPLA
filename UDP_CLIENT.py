
import sys
import socket

import errno
from time import sleep

UDP_IP = '127.0.0.1'
UDP_PORT = 55278
BUFFER_SIZE = 4096 # ?

sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM )
sckt.setblocking(0)
#sckt = socket.socket()

sckt.bind((UDP_IP, UDP_PORT))

sleep(0)


    
while True:
   

    try:
        print ("received message: host")
        data = sckt.recv(BUFFER_SIZE)
        print (data)
    except socket.error as e:
        err = e.args[0]
        if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
            sleep(1)
            print ('No data available')
            
        else:
            # a "real" error occurred
            print (e)
            sys.exit(1)
    

 
