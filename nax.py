from socket import *
from time import sleep
from threading import *
import json
from colorama import Fore 
import time
from os import system, name
import sys
import requests


class network:
    solo_server = 'localhost'
    solo_port = 8080
    ip_adress = requests.get("https://api.ipify.org?format=text").text

class conf:
    _cnt1 = True
    _cnt2 = True
def clear():
 
    if name == 'nt':    
        _ = system('cls')

    else:
        _ = system('clear')

class ListenThread(Thread):
    def __init__(self, sock):
        self.sock = sock
        super().__init__()
        self.start()

    def run(self):        
        while True:
            print(self.sock.recv(1024).decode())


def get_nick(token):
    nick = token.split("|||")
    return nick[1]

def _enter(text,tm): 

    for i in range(0,len(text)):
        print(text[i],end="")
        sleep(tm)
    print("")

def _solo():
    _enter("""
NAX IRC [Version 1.2.0]
(c) NAX IRC Server! NOX IRC server developed by thesaderror.
""",0.01)
    token = input('[!] Enter NOX Token : ')

    while conf._cnt2:
        try:
            sock = socket(AF_INET, SOCK_STREAM)
            sock.connect( (network.solo_server, network.solo_port))
            print(Fore.GREEN+f'[!] Connected server --> {network.solo_server}:{network.solo_port}')
            sock.send(f"{token}[|]{network.ip_adress}".encode())
            listener = ListenThread(sock)
            break
        except:
            print(Fore.RED+f'[error] Unable to connect to the nax_irc server!')
            print(Fore.RED+f'[Solution] Retrying in 5 seconds',end="")
            _enter("...",0.1)
            sleep(5)

    
    while conf._cnt1:
        nick_name = get_nick(token)
        message = (input(Fore.GREEN+f"[{nick_name}]: "))
        
        if(message =="exit"):
            conf._cnt1 = False
            conf._cnt2 = False
            break

        sock.send(message.encode())
        time.sleep(1)
    
            
if __name__ == "__main__":
    clear()
    _solo()