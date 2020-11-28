#!/usr/bin/env python
import socket
import threading
import time
import sys
import os
import struct
from pathlib import *

HOST = 'localhost'
PORT = 10000

def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
    except socket.error as msg:
        print (msg)
        sys.exit(1)
    print ('Waiting connection...')

    while True:
        conn, addr = s.accept()
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()

def deal_data(conn, addr):
    print ('Accept new connection from {0}'.format(addr))
    #conn.settimeout(500)
    # conn.send('Hi, Welcome to the server!')
    # 输出客户端地址

    while True:
        fileinfo_size = struct.calcsize('128sl')
        buf = conn.recv(fileinfo_size)
        if buf:
            filename, filesize = struct.unpack('128sl', buf)
            # print(filename.decode())
            fn = filename.decode().strip('\00')
            
            p = Path(__file__).resolve().parent
            new_filename = p.joinpath('new_' + fn)

            # new_filename = os.path.join('./', 'new_' + fn)

            recvd_size = 0  # 定义已接收文件的大小
            fp = open(new_filename, 'wb')
            print( '>>> start receiving...')

            print ('file new name is {0}, filesize is {1}'.format(new_filename,
                                                                 filesize))

            while not recvd_size == filesize:
                if filesize - recvd_size > 1024:
                    data = conn.recv(1024)
                    recvd_size += len(data)
                else:
                    data = conn.recv(filesize - recvd_size)
                    recvd_size = filesize
                fp.write(data)
            fp.close()
            print( '     <<<< end receive...')
        conn.close()
        break


if __name__ == '__main__':
    socket_service()