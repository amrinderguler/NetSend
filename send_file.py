import socket
import os
from tkinter import filedialog
def send_file():
    filename = filedialog.askopenfilename()
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect(("localhost",9999))

    file_path = filename
    file = open(file_path,"rb")
    file_size = os.path.getsize(file_path)
    print("The size of file is : ",file_size)

    client.send(os.path.basename(filename).encode('utf-8'))
    client.send(str(file_size).encode('utf-8'))

    data = file.read()
    client.sendall(data)
    client.send(b"<END>")

    file.close()
    client.close()