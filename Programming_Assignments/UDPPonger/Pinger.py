# UDPPinger.py
from socket import *
from time import *

serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

clientSocket.settimeout(1)
for i in range(0,10):
    try:
        message = 'Ping ' + str(i) + ' ' + ctime()
        time_start = time()
        clientSocket.sendto(message.encode(),('localhost',serverPort))
        modifiedMessage,serverAddress = clientSocket.recvfrom(2048)
        time_end = time()
        # message from server
        print(modifiedMessage.decode())
        # calculate the time
        print('this packet costs ' + str(time_end-time_start) +' seconds')

    except timeout:
        print('Request timed out')


clientSocket.close();
