
import socket
# function to check if
# character is operator or not
 
 
def isOperator(x):
 
    if x == "+":
        return True
 
    if x == "-":
        return True
 
    if x == "/":
        return True
 
    if x == "*":
        return True
 
    return False
 
# Convert postfix to Prefix expression
 
 
def postToPre(post_exp):
 
    s = []
 
    # length of expression
    length = len(post_exp)
 
    # reading from right to left
    for i in range(length):
 
        # check if symbol is operator
        if (isOperator(post_exp[i])):
 
            # pop two operands from stack
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
 
            # concat the operands and operator
            temp = post_exp[i] + op2 + op1
 
            # Push string temp back to stack
            s.append(temp)
 
        # if symbol is an operand
        else:
 
            # push the operand to the stack
            s.append(post_exp[i])
 
    
    ans = ""
    for i in s:
        ans += i
    return ans

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

res = postToPre(data)

# _______________________________________
conn.send(res.encode())

print("Result Sended!")
conn.close()  # close the connection


