import socket
import sys
import pickle


bufferSize = 256
host = '127.0.0.1'
port = 7845

if __name__ == '__main__':
    # get port no from command line arguments
    if len(sys.argv) != 1:
        host = str(sys.argv[1])
        port = int(str(sys.argv[2]))

    address = (host, port)
    try:
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        clientSocket.connect(address)
        print("Connection Successful")
    except socket.error as log:
        print("Error: "+log)
        sys.exit(1)


    size = clientSocket.recv(bufferSize).decode()
    print('size ', size)

    clientSocket.send('OK'.encode())

    receive_buffer = clientSocket.recv(int(size))
    print(type(receive_buffer))

    wms = pickle.loads(receive_buffer)
    print(wms)

    for layer in wms.contents:
        print(layer)


    clientSocket.close()
