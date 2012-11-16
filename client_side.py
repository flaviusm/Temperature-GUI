'''
Created on Oct 2, 2012

@author: UndergroundJesus
'''

import socket

#defining some variables for later use
HOST='127.0.0.1'
PORT=5432

class client():
    
    HOST='127.0.0.1'
    PORT=5432
    
    def send_temp(self):
        #creating the socket
        cl_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cl_soc.setsockpopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #connecting to our server
        cl_soc.connect((HOST,PORT))
        MSG = '$013'
        cl_soc.send(str(MSG))
        #receiving the answer
        print(cl_soc.recv(100))
        cl_soc.close()
        
    
    
