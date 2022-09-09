
import inquirer
import json
from inquirer.themes import *
from colorama import Fore 

class config:
    menu = ["server"]

def nax_dash_menu():
    menu = config.menu
    nax_menu = [inquirer.Checkbox(
        "nax_menu",
        message='Select Dashboard',
        choices=menu,
    )]
    nax = inquirer.prompt(nax_menu,theme=GreenPassion())
    
    for i in nax['nax_menu'] :
        print(i)