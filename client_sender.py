print('client_sender')
import sys
import io
import socket
import select
import threading
import queue
import random
import time
words = ['one','two', 'free', 'four', 'five', 'six', 'seven']
role='sender'
host ='localhost'
port = 9998
time_for_client = 1000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))
print('conected_with_server',end ='')
client.send(role.encode('utf-8'))
print(f'_as: {role}')
start = time.time()
print(f'start_send_data_to_server_next_{time_for_client}s')
while time.time()-start <= time_for_client:
    try:
        to_send = random.choice(words)
        client.send((to_send).encode('utf-8'))
        print(f'sending: {to_send}')
        time.sleep(random.randint(1,3))
    except BrokenPipeError:
        print('broken_pipe')
print('data_sending_complited')
client.close()