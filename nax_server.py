from socket import *
from time import sleep
from threading import *
import json
from colorama import Fore 
from os import system, name
import time
from modnax.nax_dash import *

class network:
    nax_server = 'localhost'
    NAX_port = 8080
    clients = []
    clients_public = []
    usernames = []
    live = 0


class conf:
    user_conf = "./modnax/database/nax_db.json"
    
    live = "./modnax/lib/dashboard/live.txt"
    usernames = "./modnax/lib/dashboard/usernames.txt"
    clients = "./modnax/lib/dashboard/clients.txt"

def _user_db(token):
    with open(conf.user_conf, 'r') as user_config:
        user_db = user_config.read()
        user_conf = json.loads(user_db)
    try:
        return user_conf["token"][token]
    except:
        pass 


def dash_clients():
    with open(conf.live, "w") as f1:
        f1.write(f"{network.live}")
        f1.close()
    with open(conf.usernames, "w") as f2:
        f2.write(f"{network.usernames}")
        f2.close()
    with open(conf.clients, "w") as f3:
        f3.write(f"{network.clients}")
        f3.close()


class ClientHandler(Thread):
    def __init__(self, nax_server, nax_addr, nax_token):
        self.sock = nax_server
        self.address = nax_addr
        self.token = nax_token.split("[|]")[0]
        self.ip_adress = nax_token.split("[|]")[1]
        network.clients.append(self)
        super().__init__()
        self.start()

    def run(self):
        network.clients_public.append(self.ip_adress)
        network.usernames.append(_user_db(self.token)["nickname"])
        network.live +=1
        print(Fore.BLUE+f'\n[--{_user_db(self.token)["nickname"]}--] connected to server! [{self.ip_adress}]\n')
        dash_clients()
        
        #print(network.clients_public)
        
        while True:
            (self.ip_adress,_user_db(self.token)["nickname"])
            try:
                if(_user_db(self.token)["banned"]=="false"):
                    try:
                        text = self.sock.recv(1024).decode()
                        if(_user_db(self.token)["color"] == "red"):
                            nax_send = Fore.RED+f'<{_user_db(self.token)["nickname"]}/{_user_db(self.token)["role"]}> {text}'
                            print(Fore.RED+f'<{_user_db(self.token)["nickname"]}/{_user_db(self.token)["role"]}> {text}')
                            
                        elif(_user_db(self.token)["color"] == "cyan"):
                            nax_send = Fore.CYAN+f'<{_user_db(self.token)["nickname"]}/{_user_db(self.token)["role"]}> {text}'
                            print(Fore.CYAN+f'<{_user_db(self.token)["nickname"]}/{_user_db(self.token)["role"]}> {text}')
                            
                        elif(_user_db(self.token)["color"] == "blue"):
                            nax_send = Fore.BLUE+f'<{_user_db(self.token)["nickname"]}/{_user_db(self.token)["role"]}> {text}'
                            print(Fore.BLUE+f'<{_user_db(self.token)["nickname"]}/{_user_db(self.token)["role"]}> {text}')
                        
                        elif(_user_db(self.token)["color"] == "yellow"):
                            nax_send = Fore.YELLOW+f'<{_user_db(self.token)["nickname"]}/{_user_db(self.token)["role"]}> {text}'
                            print(Fore.YELLOW+f'<{_user_db(self.token)["nickname"]}/{_user_db(self.token)["role"]}> {text}')
                        
                        else:
                            nax_send = Fore.BLUE+f'<{_user_db(self.token)["nickname"]}/new> {text}'
                            print(Fore.BLUE+f'<{_user_db(self.token)["nickname"]}/new> {text}')
                    except:
                        nax_send = Fore.BLUE+f'<{_user_db(self.token)["nickname"]}/new> {text}'
                        print(Fore.BLUE+f'<{_user_db(self.token)["nickname"]}/new> {text}')
                        
                    for client in network.clients:
                        client.sock.send(nax_send.encode())
                else:
                    pass




            except ConnectionResetError:
                disconnect_msg = Fore.RED+f'\n|{_user_db(self.token)["nickname"]}| disconnected!\n'
                network.live -= 1
                print(disconnect_msg)
                network.clients.remove(self)
                for client in network.clients:
                    client.sock.send(disconnect_msg.encode())
                self.sock.close()
                break   

def clear():
    if name == 'nt':_ = system('cls')
    else : _ = system('clear')

def start_server():
    NAX_sock = socket(AF_INET, SOCK_STREAM)
    NAX_sock.bind( (network.nax_server, network.NAX_port) )
    NAX_sock.listen(5)
    print(Fore.BLUE+f'-NAX IRC server started at {network.nax_server}:{network.NAX_port}-')

    while True:
        nax_server, nax_addr = NAX_sock.accept()
        nax_token = nax_server.recv(1024).decode()
        client = ClientHandler(nax_server, nax_addr, nax_token)

if __name__ == '__main__':
    clear()
    start_server()
    
    