
import socket

def isOperand(x):
    return ((x >= 'a' and x <= 'z') or
            (x >= 'A' and x <= 'Z'))
 
# Get Infix for a given postfix
# expression
def getInfix(exp) :
 
    s = []
 
    for i in exp:    
         
        # Push operands
        if (isOperand(i)) :        
            s.insert(0, i)
             
        # We assume that input is a
        # valid postfix and expect
        # an operator.
        else:
         
            op1 = s[0]
            s.pop(0)
            op2 = s[0]
            s.pop(0)
            s.insert(0, "(" + op2 + i +
                             op1 + ")")
             
    # There must be a single element in
    # stack now which is the required
    # infix.
    return s[0]

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

res = getInfix(data)
# _______________________________________
conn.send(res.encode())

print("Result Sended!")
conn.close()  # close the connection


