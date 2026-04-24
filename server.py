print('server')
import sys
import io
from _thread import start_new_thread
import socket
import select
import threading
import queue
import sys
import os
import time
import subprocess
import re
roles = {'sender': None, 'reader': None}
host ='localhost'
port = 9998
message_size = 2048
data_from_client= queue.Queue()
lock = threading.Lock() # только один поток на конкретный участок кода в конкретный момент времени
################# удаление не нужных процессов с порта ###################
def delete_pids_with_port(port):
    result = subprocess.run(['powershell', '-Command', 'netstat -ano | select-string 9998'], capture_output=True, text=True, encoding='cp866')
    PIDS = [re.split('[ ]+',i)[5] for i in (str(result).split('\\n')[1:-3])]
    print(f'{port} PIDs for delete: ',PIDS)
    for pid in PIDS:
        subprocess.run(f'taskkill /PID {pid} /F')
        print(f'{pid} - deleted')
########################### работа с клиентами сервера ###################
def work_with_client(client, role):
    try:
        #---------------------sender-----------------
        if role == 'sender':
            while True:
                s, _, _ = select.select([client], [], [], 5)
                if client not in s:
                    print('sender_socket_problem')
                    break
                data = client.recv(1024).decode('utf-8')
                if not data:
                    time.sleep(5)
                    data = client.recv(1024).decode('utf-8')
                    if not data:
                        print('no_new_data')
                        break
                data_from_client.put(data)
                print(f'from_sender: {data}')
        #-------------------reader-----------------------        
        elif role == 'reader':
            while data_from_client.empty():
                print('no_data___wait')
                time.sleep(10)
                continue
            while True:
                _, s, _ = select.select([], [client], [], 5)
                if client not in s:
                    print('reader_socket_problem')
                    break
                if data_from_client.empty():
                    time.sleep(5)
                    if data_from_client.empty():
                        print('no_data_in_queue')
                        break
                data = data_from_client.get()
                client.send((data+ "\n").encode('utf-8'))
                print(f'to_reader: {data}')
        #-------------------------------------------------
    except ConnectionResetError:
        print(f'{role}_reset_connection')
    except Exception as e:
        print(f'{e}')
    finally:
        client.close()
        roles[role] = None
        print(f'{role}_client_closed')
########################### запуск сервера ###############################
delete_pids_with_port(port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.bind((host,port))
server.listen(2)
print('server_started')
while True:
    print('server_waiting_clients')
    client, c_address = server.accept()
    lock.acquire() # попытка захвата блокировки, если свободна, то берет, иначе ждет
    print(f'new_client: {c_address}')
    # s, _, _= select.select([client], [], [], 3)
    # if not s:
    #     client.close()
    #     print(f'\tno_role_disconected')
    #     continue
    # -------------------streamer----------------------------------------
    s, _, _= select.select([client], [], [], 3)
    if not s:
        role = 'reader'
        roles[role] = client
        print(f'\tnew_streamer_as_{role}_client')
        client_thread = threading.Thread(target = work_with_client, args = (client,role))
        client_thread.start()
        lock.release() #освобождение заблокированного потока
        continue
    # ----------------------------------------------------------------
    role = client.recv(6).decode('utf-8')
    if role not in roles.keys():
        client.close()
        print(f'\twrong_role_disconected: {role}')
        continue
    if roles[role] is not None:
        client.close()
        print(f'\talready_have_role:{role} disconected')
        continue
    roles[role] = client
    print(f'\tnew_{role}_client')
    client_thread = threading.Thread(target = work_with_client, args = (client,role))
    client_thread.start()
    lock.release() #освобождение заблокированного потока
    
server.close()