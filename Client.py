import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 12345  ))
print("Connected to server")
fh=open("story.txt","r")    
data=fh.readlines()  
client_socket.send(' '.join(data).encode())
print("Server: Flie Recived")
client_socket.close()
