
import socket

# Python Program to convert prefix to Infix
def prefixToInfix(prefix):
    stack = []
     
    # read prefix in reverse order
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
             
            # symbol is operand
            stack.append(prefix[i])
            i -= 1
        else:
           
            # symbol is operator
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
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

#_________________________________________

res = prefixToInfix(data)
# _______________________________________
conn.send(res.encode())

print("Result Sended!")
conn.close()  # close the connection


