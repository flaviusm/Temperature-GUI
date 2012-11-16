'''
Created on Oct 2, 2012

@author: UndergroundJesus
'''
import Tkinter as tk
from Tkinter import *
import socket



HOST='127.0.0.1'
PORT=5432

class guiclass():

    def __init__(self):
           
        self.other = tk.Toplevel()
        self.other.title("My Temperature GUI")
        self.otherlabel = tk.Label(self.other, text='SEND YOUR COMMAND TO RS485', relief = tk.RIDGE)
        self.otherlabel.pack(side=tk.TOP, fill = tk.BOTH, expand = tk.YES)
        self.otherbutton1 = tk.Button(self.other, text='TEMPERATURE', command=self.send_temp).pack(side=tk.TOP)
        self.otherbutton2 = tk.Button(self.other, text='QUIT', command=self.other.quit).pack(side=tk.BOTTOM)
        self.outputvalue = tk.StringVar()
	self.otherlabel1 = tk.Label(self.other, textvariable =self.outputvalue).pack(side=tk.BOTTOM)
       
   
        
    def send_temp(self):
        #creating the socket
        cl_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cl_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #connecting to our server
        cl_soc.connect((HOST,PORT))
        MSG = '$013'
        cl_soc.send(str(MSG))
        #receiving the answer
        self.outputvalue.set(str(cl_soc.recv(100)))
        cl_soc.close()
        
   
        
if __name__ == '__main__':
    
    win = tk.Frame()
    win.pack()
    
    
    guiclass()
    
    win.mainloop( )


