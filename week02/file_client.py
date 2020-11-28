#!/usr/bin/env python
import socket
import os
import sys
import struct
from pathlib import *

HOST = 'localhost'
PORT = 10000

print ('type exit! to quit, or input filename for transfer')

def socket_client():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
    except socket.error as msg:
        print (msg)
        sys.exit(1)

    # print (s.recv(1024))

    while True:
        filepath = input('input file >>') #raw_input
        
        # 设定退出条件
        if filepath == 'exit!':
            break

        # 获得python脚本的绝对路径
        p = Path(__file__).resolve().parent

        filepath = p.joinpath(filepath)
        print ('client filepath: {0}'.format(filepath))

        if os.path.isfile( filepath ):
            # 定义定义文件信息。128s表示文件名为128bytes长，l表示一个int或log文件类型，在此为文件大小
            fileinfo_size = struct.calcsize('128sl')

            # 定义文件头信息，包含文件名和文件大小
            # print(os.path.basename(filepath))
            # print(os.stat(filepath).st_size)
            fhead = struct.pack('128sl', os.path.basename(filepath).encode(), os.stat(filepath).st_size)

            s.send(fhead)

            fp = open(filepath, 'rb')
            while True:
                data = fp.read(1024)
                if not data:
                    print ('{0} file send over...'.format(filepath))
                    break
                s.send(data)
                
            print ('>>> one file passed over, type exit! to quit or try another')

    s.close()

if __name__ == '__main__':
    socket_client()
