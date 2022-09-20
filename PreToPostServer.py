
import socket

server_socket = socket.socket()  # creating socket
port = 5000  # initiate port no 

print('Socket created')
server_socket.bind(('localhost',port))  # bind host address and port together

# configure how many client the server can listen simultaneously
server_socket.listen(2)

print('Waiting for connections')
conn, address = server_socket.accept()  # accept new connection
print("Connected with: " + str(address))

# receive data stream. it won't accept data packet greater than 1024 bytes (beffer size)
data = conn.recv(1024).decode()

# Stack for storing operands
stack = []
 
operators = set(['+', '-', '*', '/', '^'])
 
# Reversing the order
data = data[::-1]
 
# iterating through individual tokens
for i in data:
 
    # if token is operator
    if i in operators:
 
        # pop 2 elements from stack
        a = stack.pop()
        b = stack.pop()
 
        # concatenate them as operand1 +
        # operand2 + operator
        temp = a+b+i
        stack.append(temp)
 
    # else if operand
    else:
        stack.append(i)
res = ""

for i in stack:
    res+=i
conn.send(res.encode())

print("Result Sended!")
conn.close()  # close the connection


