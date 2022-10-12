import socket

serverName = 'localhost'
serverPort = 14000
serverAddress = (serverName, serverPort)
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(serverAddress)

kerkesa = input("(IP, NRPORTIT, NUMERO, ANASJELLTAS, PALINDROM, KOHA, LOJA, GLG, KONVERTO, GRG, QUAD)> ")
connected = True
while connected:
    if(len(kerkesa)==0):
        print("Nuk ka komand blank je shkyqur nga serveri")
        connected = False
        dissconect = "shkyqu"
        clientSocket.send(dissconect.encode())
        break
    else:
        if(kerkesa == "shkyqu"):
            connected = False
            clientSocket.send(kerkesa.encode())
            print("Lidhja eshte mbyllur")
        else:
            clientSocket.send(kerkesa.encode())
            msg = clientSocket.recv(128).decode()
            print(msg)
            kerkesa = input("(IP, NRPORTIT, NUMERO, ANASJELLTAS, PALINDROM, KOHA, LOJA, GLG, KONVERTO, GRG, QUAD)> ")