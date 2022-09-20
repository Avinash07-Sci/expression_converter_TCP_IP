
import socket

def isOperator(c):
    return (not (c >= 'a' and c <= 'z') and not(c >= '0' and c <= '9') and not(c >= 'A' and c <= 'Z'))
 
def getPriority(C):
    if (C == '-' or C == '+'):
        return 1
    elif (C == '*' or C == '/'):
        return 2
    elif (C == '^'):
        return 3
    return 0
 

def infixToPrefix(infix):
    operators = []
    operands = []
 
    for i in range(len(infix)):
        
        if (infix[i] == '(' ):
            operators.append(infix[i])
 
        elif (infix[i] == ')'):
            while (len(operators)!=0 and (operators[-1] != '(' )):
                op1 = operands[-1]
                operands.pop()
                op2 = operands[-1]
                operands.pop()
                op = operators[-1]
                operators.pop()
                tmp = op + op2 + op1
                operands.append(tmp)
            operators.pop()
        elif (not isOperator(infix[i])):
            operands.append(infix[i] + "")
 
        else:
            while (len(operators)!=0 and getPriority(infix[i]) <= getPriority(operators[-1])):
                op1 = operands[-1]
                operands.pop()
 
                op2 = operands[-1]
                operands.pop()
 
                op = operators[-1]
                operators.pop()
 
                tmp = op + op2 + op1
                operands.append(tmp)
            operators.append(infix[i])
 
    while (len(operators)!=0):
        op1 = operands[-1]
        operands.pop()
 
        op2 = operands[-1]
        operands.pop()
 
        op = operators[-1]
        operators.pop()
 
        tmp = op + op2 + op1
        operands.append(tmp)
    return operands[-1]
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

res = infixToPrefix(data)
# _______________________________________
conn.send(res.encode())

print("Result Sended!")
conn.close()  # close the connection


