
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
expression = conn.recv(1024).decode()

#_________________________________________
Operators = set(['+', '-', '*', '/', '(', ')', '^'])  # collection of Operators

Priority = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities of Operators

stack = [] # initialization of empty stack

res = '' 



for character in expression:

    if character not in Operators:  # if an operand append in postfix expression

        res+= character

    elif character=='(':  # else Operators push onto stack

        stack.append('(')

    elif character==')':

        while stack and stack[-1]!= '(':

            res+=stack.pop()

        stack.pop()
    else: 

        while stack and stack[-1]!='(' and Priority[character]<=Priority[stack[-1]]:

            res+=stack.pop()

        stack.append(character)

while stack:

    res+=stack.pop()
# _______________________________________
conn.send(res.encode())

print("Result Sended!")
conn.close()  # close the connection


