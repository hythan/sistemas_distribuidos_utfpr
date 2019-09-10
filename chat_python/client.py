import socket
import time

# Criar o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar ao servidor com ip e porta
sock.connect(('localhost', 9003))

while True:
    # Leia o tamanho da mensagem
    expected_data_size = int(sock.recv(4).decode())
    print("Tamanho de dado esperado = {}".format(expected_data_size))

    received_data = ''
    while len(received_data) < expected_data_size:
        # Ler o dado recebido
        received_data += sock.recv(4).decode()
        print("Tamanho do dado {}".format(len(received_data)))
    print(received_data)


    # Tamanho da mensagem
    mensagem = raw_input("Say something:").strip()
    send_data_size = len(mensagem)
    sock.sendall(str(send_data_size).zfill(4).encode())

    # Enviar a mensagem
    sock.sendall(mensagem.encode())

    # Finalizar a conexao:
    if mensagem == 'see ya':
        sock.close()

