
import socket

port = 5000  # socket server port number

client_socket = socket.socket()  # instantiate
client_socket.connect(('localhost', port))  # connect to the server

message = input("InFix Expression: ")  # take input
client_socket.send(message.encode())  # send message

res = client_socket.recv(1024).decode()

print("PostFix of given Expression: ",res)
client_socket.close()  # close the connection