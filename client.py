import threading
import socket

HOST = '127.0.0.1'
PORT = 50000
BUFFER_SIZE = 2048

def main():
    # os parâmetros do método socket indicam a família de protocolo (IPV4)
    # e o tipo do protocolo (TCP)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((HOST, PORT))
    except:
        return print("Não foi possível se conectar ao servidor")
    
    username = input("Usuário:")
    print("Conectado")

    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=sendMessages, args=[client, username])

    thread1.start()
    thread2.start()


def receiveMessages(client):
    while True:
        try:
            msg = client.recv(BUFFER_SIZE).decode('utf-8')
            print(msg+"/n")
        except:
            print("Não foi possível permanecer conectado ao servidor")
            print("Pressione <Enter> para continuar...")
            client.close()
            break


def sendMessages(client, username):
    while True:
        try:
            msg = input()
            client.send(f'<{username}> {msg}'.encode('utf-8'))
        except:
            return


main()