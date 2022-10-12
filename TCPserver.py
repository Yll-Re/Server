import socket
import threading
import random
import cmath

print("Fillon Serveri...")

serverName = 'localhost'
serverPort = 14000
serverAddress = (serverName, serverPort)

def IPADRESA():
    return socket.gethostbyname(socket.gethostname())

def NRPORTIT():
    return str(serverAddress[1])

def NUMEROZ(text):
    zanoret = ['a','A','e','E',u'\u00EB',u'\u00CB','i','I','o','O','u','U','y','Y']
    count = 0
    for ch in text:
        if(ch in zanoret):
            count += 1
    return count

def NUMEROB(text):
    bashkëtingëlloreve = ['b','B','c','C','Ç','ç','d','D','f','F','g','G','h','H','j','J','k','K','l','L','m','M','n','N','p','P','q','Q','r','R','s','S','t','T','v','V','x','X','z','Z']
    count = 0
    for ch in text:
        if(ch in bashkëtingëlloreve):
            count += 1
    return count    

def ANASJELLTAS(text):
    backText = text[::-1]
    return backText.strip()

def PALINDROM(text):
    palindromText = text[::-1]
    return str(palindromText.strip())

def LOJA():
    numbers = []

    for i in range(0, 5):
        numbers.append(random.randint(1, 35))
    
    numbers.sort()
    randomNumbers = str(numbers)
    return randomNumbers

def GCF(x,y):
    if(y==0):
        return x
    else:
        return GCF(y,x%y)

def KONVERTIMI(convert,value):
    if convert == "cmNeInch":
        result = value / 2.54
    elif convert == "inchNeCm":
        result = value * 2.54
    elif convert == "kmNeMiles":
        result = value / 1.609
    elif convert == "mileNeKm":
        result = value * 1.609
    else:
        result = "Nuk keni zgjedhur konvertimin mire"
    return result

def GLG(choice):

    from random import randint

    table = ["Gure", "Leter", "Gersher"]

    randomGLG = table[randint(0,2)]

    if choice == randomGLG:
        return "Barazi!"
    elif choice == "Gure":
        if randomGLG == "Leter":
            return("Humbe", randomGLG, "mbeshtjell", choice)
        else:
            return("Fitove", choice, "thyen", randomGLG)
    elif choice == "Leter":
        if randomGLG == "Gersher":
            return("Humbe", randomGLG, "prejne", choice)
        else:
            return("Fitove", choice, "mbeshtjell", randomGLG)
    elif choice == "Gersher":
        if randomGLG == "Gure":
            return("Humbe", randomGLG, "thyen", choice)
        else:
            return("Fitove", choice, "prejne", randomGLG)
    else:
        return("Zgjedh mes Gure, Leter, Gersher")

def QUAD(a,b,c):

    d = ((b**2) - (4*a*c))

    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)

    return(sol1, sol2)

    


def client(conn, serverAddress):
    print(f"Lidhje e re nga {serverAddress}")

    connected = True
    while connected:
        try:
            msg = conn.recv(128).decode("utf-8")
        except socket.error:
            print(f"klienti {serverAddress} eshte shkyqur")
            print(f"Numri i lidhjeve eshte {threading.activeCount()-2}")
            break

        Getmsg = str(msg)
        msgSplit = Getmsg.rsplit(" ")
        text= ""
        msgLength = len(msgSplit)
        for x in range(1, msgLength):
            text += msgSplit[x]
            if(x!=msgSplit):
                text += " "
        if not msg:
            break
        elif msgSplit[0] == "shkyqu":
                connected = False
                print(f"klienti {serverAddress} eshte shkyqur")
                conn.close()
                print(f"Numri i lidhjeve eshte {threading.activeCount()-2}")
        elif msgSplit[0] == "IP":
                msg = "IP-ja jote eshte : " + IPADRESA()
                conn.send(msg.encode())
        elif msgSplit[0] == "NRPORTIT":
                msg = "Porta jote eshte : " + NRPORTIT()
                conn.send(msg.encode())
        elif msgSplit[0] == "NUMERO":
                msg = "Numri i zanoreve eshte: " + str(NUMEROZ(text)) + " Ndersa i bashkëtingëlloreve: " + str(NUMEROB(text))
                conn.send(msg.encode())
        elif msgSplit[0] == "ANASJELLTAS":
                msg = "Teksti i kthyer mbrapsht eshte: " + str(ANASJELLTAS(text))
                conn.send(msg.encode())
        elif msgSplit[0] == "PALINDROM":
            x = text.strip()
            w = ""
            for i in x:
                w = i + w
            
            if (x==w):
                msg = "Teksti eshte palindrom"
                conn.send(msg.encode())
            else:
                msg = "Teksti nuk eshte palindrom"
                conn.send(msg.encode())
        elif msgSplit[0] == "KOHA":
            from datetime import datetime

            now = datetime.now()

            current_time = now.strftime("%H:%M:%S")
            
            msg = ("Koha tani eshte: " + current_time)
            conn.send(msg.encode())
        elif msgSplit[0] == "LOJA":
                msg = "5 numbra nga 1 - 35: " + LOJA()
                conn.send(msg.encode())
        elif msgSplit[0] == "GCF":
                x = int(msgSplit[1])
                y = int(msgSplit[2])
                msg = "GCF: " + str(GCF(x,y))
                conn.send(msg.encode())
        elif msgSplit[0] == "KONVERTO":
                convert = msgSplit[1]
                value = float(msgSplit[2])
                msg = "Konvertimi: " + str(KONVERTIMI(convert,value))
                conn.send(msg.encode())
        elif msgSplit[0] == "GLG":
                choice = msgSplit[1]
                msg = str(GLG(choice))
                conn.send(msg.encode())
        elif msgSplit[0] == "QUAD":
                a = float(msgSplit[1])
                b = float(msgSplit[2])
                c = float(msgSplit[3])
                msg = "Zgjidhjet e kti ek. jane: " + str(QUAD(a,b,c))
                conn.send(msg.encode())
        else:
                msg = "Kjo kerkes nuk egziston"
                conn.send(msg.encode())

def main():

    serverAddress = (serverName, serverPort)
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(serverAddress)
    serverSocket.listen()
    print(f"Serveri eshte vendosur ne {serverName}:{serverPort}")

    while True:
        conn, serverAddress = serverSocket.accept()
        thread = threading.Thread(target=client, args=(conn, serverAddress))
        thread.start()
        print(f"Numri i lidhjeve eshte {threading.activeCount()-1}")

if __name__ == "__main__":
    main()


