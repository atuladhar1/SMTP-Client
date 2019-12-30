from socket import *
import ssl
import base64

# the message to be sent.
msg = "\r\nI love computer networks!\r\n"
endmsg = "\r\n.\r\n"
# the server for the email.
mailserver =("smtp.gmail.com",587)

# emailaddress 
email = "safalis@sexyboi.com"
# password
password = "sexyboi69"

# open a client side socket for the operations
with socket(AF_INET, SOCK_STREAM) as clientsocket:

    # connect to the gmail server and print the return
    clientsocket.connect(mailserver)
    recv= clientsocket.recv(1024).decode()
    print(recv)
    if  recv[:3]!= "220":
        print ("220 reply not recieved from Server")
        
    #send Helo command and print the return
    helocommand ='HELO Alice\r\n'
    clientsocket.send(bytes(helocommand,"utf-8"))
    recv1= clientsocket.recv(1024).decode()
    print(recv1)
    if recv1[:3]!= "250":
        print("250 reply not received from server.")
    # Ask the server to start the Transport Layer Protocol

    clientsocket.send(bytes("STARTTLS\r\n","utf-8"))
    recv2=clientsocket.recv(1024).decode()
    print(recv2)
    securesocket =ssl.wrap_socket(clientsocket,ssl_version=ssl.PROTOCOL_SSLv23)

    # Initialize the login process
    securesocket.send(bytes("AUTH LOGIN\r\n","utf-8"))
    recv2=securesocket.recv(1024).decode()
    print(recv2)

    # Send the username address 
    securesocket.send(base64.b64encode(bytes(email,"utf-8")))
    securesocket.send(bytes("\r\n","utf-8"))
    recv2=securesocket.recv(1024).decode()
    print(recv2)
    
    # Send the password for that address
    securesocket.send(base64.b64encode(bytes(password,"utf-8")))
    securesocket.send(bytes("\r\n","utf-8"))
    recv2= securesocket.recv(1024).decode()
    print(recv2)

    # Send the senders mail address
    securesocket.send((bytes("MAIL FROM:<lijegod@gmail.com>","utf-8")))
    securesocket.send(bytes("\r\n","utf-8"))
    recv2= securesocket.recv(1024).decode()
    print(recv2)

    # Send the recievers mail address
    securesocket.send(bytes("RCPT TO:<atuladhar1@gmail.com>","utf-8"))
    securesocket.send(bytes("\r\n","utf-8"))
    recv2 =securesocket.recv(1024).decode()
    print(recv2)

    # Send the DATA command
    securesocket.send(bytes("DATA\r\n","utf-8"))
    recv2= securesocket.recv(1024).decode()
    print(recv2)

    # Send the body of the mail
    securesocket.send(bytes(msg,"utf-8"))
    securesocket.send(bytes(endmsg,"utf-8"))
    recv2=securesocket.recv(1024).decode()
    print(recv2)

    # Send the QUIT message to the server
    securesocket.send(bytes("QUIT\r\n","utf-8"))
    recv2= securesocket.recv(1024).decode()
    print(recv2)