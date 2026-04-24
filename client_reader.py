print('client_reader')
import sys
import io
import socket
import select
import threading
import queue
import random
import time
role='reader'
host ='localhost'
port = 9998
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))
print('conected_with_server',end ='')
client.send(role.encode('utf-8'))
print(f'_as: {role}')
print(f'start_read_data_from_server')
while True:
    try:
        ####
        s, r, _ = select.select([client], [client], [], 5)
        if client not in s and client not in r:
            print('reader_socket_problem')
            break
        #####
        data = client.recv(1024).decode('utf-8')
        if not data:
            time.sleep(5)
            data = client.recv(1024).decode('utf-8')
            if not data:
                print('no_new_data')
                break
        print(f'readed_from_server: {data}')
    except ConnectionResetError:
        print('reset_connection_with_server')
        client.close()
    except Exception as e:
        print(f'{e}')
        client.close()
client.close()
print('close_connection')