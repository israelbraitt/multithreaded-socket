import threading
import socket

HOST = 'localhost'
PORT = 50000
BUFFER_SIZE = 2048

clients = []

def main():
    # os parâmetros do método socket indicam a família de protocolo (IPV4)
    # e o tipo do protocolo (TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        server.bind(('', PORT))
        server.listen()
        print("Aguardando conexão de um cliente")
    except:
        return print("Não foi possível iniciar o servidor")

    while True:
        conn_client, addr_client = server.accept()
        print("Conectado em", addr_client)
        clients.append(conn_client)

        thread = threading.Thread(target=messagesTreatment, args=[conn_client])
        thread.start()         


def messagesTreatment(client):
    while True:
        try:
            data = client.recv(BUFFER_SIZE)
            msg = data.decode()
            print("Mensagem recebida:", msg)
        except:
            deleteClient(client)
            break


def sendMessages(msg, client):
    try:
        client.send(msg.encode('utf-8'))
    except:
        deleteClient(client) 


def broadcast(msg, client):
    for client_item in clients:
        if (client_item != client):
            try:
                client_item.send(msg)
            except:
                deleteClient(client_item)


def deleteClient(client):
    clients.remove(client)


main()