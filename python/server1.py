import socket
import _thread as thread
import threading
import sys
import datetime
import pickle
from datetime import date
from owslib.wms import WebMapService

# ip address for geo-servers
ip1 = "http://10.14.1.163:8080/geoserver/wms"
ip2 = "http://10.14.1.201:8080/geoserver/wms"

g1 = '10.14.1.163:8080'
g2 = '10.14.1.201:8080'
g = g1
one = 1
server = ip1

# default values for server
bufferSize = 256
host = '127.0.0.1'
port = 7845
maxClient = 1
VERSION = '1.1.1'


def scheduler(clientSocket, address, server, VERSION):
    global one
    if one==1:
        server = ip2
        one = 0
        g = g2
    else:
        server = ip1
        g = g1
        one = 1
    print('senidng reply from GeoServer: '+g)
    # print(one)
    wms = WebMapService( server, version=VERSION)
    print(wms.identification.type)
    serial_wms = pickle.dumps(wms)

    size = sys.getsizeof(serial_wms)
    clientSocket.send(str(size).encode())

    clientSocket.recv(bufferSize)
    #send_buffer = wms
    clientSocket.send(serial_wms)
    return wms


if __name__ == '__main__':

    # get port no from command line arguments
    if len(sys.argv) != 1:
        host = str(sys.argv[1])
        port = int(str(sys.argv[2]))

    # create socket
    address = (host, port)
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind(address)
    serverSocket.listen()

    # get geo-server address    
    
    print('load balancer running on: 10.14.1.163:7845')
    while 1:
        # connect client
        clientSocket, address = serverSocket.accept()

        # schedule request
        thread.start_new_thread(scheduler, (clientSocket, address, server, VERSION))