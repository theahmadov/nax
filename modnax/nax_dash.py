import inquirer
import json
from inquirer.themes import *
from colorama import Fore 
from modnax.nax_start import *
from modnax.lib.load import *
from modnax.lib.clear import * 
from time import sleep
from rich.align import Align
from rich.console import Console
from rich.panel import Panel

class config:
    menu = ["server"]
    fcount = "./modnax/lib/dashboard/clients.txt"
    fusernames = "./modnax/lib/dashboard/usernames.txt"
    fclients = "./modnax/lib/dashboard/clients.txt"

class data:
    count = 0
    usernames = []
    clients = []

def get_clients_count():
    with open(config.fcount,"r") as f:
        data.count=f.read()
        f.close()
    with open(config.fusernames, "r") as f2:
        f2.write(f"{data.usernames}")
        f2.close()
    with open(config.fclients, "r") as f3:
        f3.write(f"{data.clients}")
        f3.close()


def recv_clients(clients_public,usernames):
    from prettytable import PrettyTable
    nax_data = PrettyTable(["username", "client"])
    for i in range(0,len(clients_public)):
        nax_data.add_row([usernames[i],clients_public[i]])
    print(nax_data)

def print_live():
    from rich import print
    from rich.panel import Panel
    print(Panel("Live Users, [red]World!", title="Live Users"))

def print_dash():
    print(f"""
    Alive Users : {data.count}
    Clients : {data.clients}
    Users : {data.usernames}
    """)

def server_dashboard(): 
    while True:
        clear()
        get_clients_count()



def start_screen():
    console = Console()

    with console.screen(style="bold white on red") as screen:
        text = Align.center("[blink]Starting nax_dash...[/blink]", vertical="middle")
        screen.update(Panel(text))
        sleep(5)
def nax_dash_menu():
    start_screen()

    menu = config.menu
    nax_menu = [inquirer.Checkbox(
        "nax_menu",
        message='Select Dashboard',
        choices=menu,
    )]
    nax = inquirer.prompt(nax_menu,theme=GreenPassion())
    
    for i in nax['nax_menu'] :
        if(i== "server"):
            server_dashboard()