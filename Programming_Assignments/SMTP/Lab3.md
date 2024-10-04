## SMTP Lab

需要额外添加用户验证这个步骤。

邮箱还有密码都没写上来。

```python
from socket import *
import base64


# campus email server
mailserver = ('mail.stu.xidian.edu.cn',25)#Fill in start #Fill in end

# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start 

clientSocket = socket(AF_INET, SOCK_STREAM) # the second para represents the protocol is tcp
clientSocket.connect(mailserver)

#Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')
    
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send AUTH LOGIN command and print server response.
authlogin = 'auth login\r\n'
clientSocket.send(authlogin.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != '334':
    print('334 reply not received from server.')

# send account
user = '*'
userCommand = base64.b64encode(user.encode()) + b'\r\n'
clientSocket.send(userCommand)
recv3 = clientSocket.recv(1024).decode()
print(recv3)
if recv3[:3] != '334':
    print('334 reply not received from server.')



# send password
userpass = '*'
userpass = base64.b64encode(userpass.encode()) + b'\r\n'
clientSocket.send(userpass)
recv4 = clientSocket.recv(1024).decode()
print(recv4)
if recv4[:3] != '235':
    print('235 reply not received from server.')
 
# Send MAIL FROM command and print server response.
# Fill in start

mailfromCommand = 'MAIL FROM: <' + user + '>\r\n'
clientSocket.send(mailfromCommand.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
if recv5[:3] != '250':
     print('250 reply not received from server.')

# Fill in end

# Send RCPT TO command and print server response. 
# Fill in start
rcptCommand = 'RCPT TO: <*>\r\n'
clientSocket.send(rcptCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
if recv6[:3] != '250':
    print('250 reply not received from server.')

# Fill in end

# Send DATA command and print server response. 
# Fill in start
dataCommand = 'DATA\r\n'
clientSocket.send(dataCommand.encode())
recv7 = clientSocket.recv(1024).decode()
print(recv7)
if recv7[:3] != '354':
    print('354 reply not received from server.')

# Fill in end

# Send message data.
# Fill in start

message = 'From: '+user+'\r\nTo: *\r\nSubject: chat\r\n\r\nYou are so cute.\r\n'
clientSocket.send(message.encode())

# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send('.\r\n'.encode()) 
recv8 = clientSocket.recv(1024).decode()
print(recv8)
if recv8[:3] != '250':
    print('250 reply not received from server.')

# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitCommand = 'QUIT\r\n'
clientSocket.send(quitCommand.encode())
recv9 = clientSocket.recv(1024).decode()
print(recv9)
if recv9[:3] != '221':
   print('221 reply not received from server.')
# Fill in end
```

运行客户端，收到服务端的回复：

![image-20241004171328356](SMTP Lab/image-20241004171328356.png)

收到消息

![image-20241004171214561](C:\Users\1\AppData\Roaming\Typora\typora-user-images\image-20241004171214561.png)