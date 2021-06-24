#!/usr/bin/env python

import socket

# This is the IP of the host
TCP_IP = '192.168.1.106'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)

while True:
    data = s.recv(BUFFER_SIZE)
    print("received data:", data)
s.close()