from colorama import Fore 
import requests , os , time
from modnax.nax_start import *
from modnax.lib.clear import *
from modnax.lib.load import *

class config:
    menu = open("./modnax/assets/.menu")
    wait_close = 30
    
def getmenu():
    menu = config.menu.read().splitlines()
    return menu

def _modnax():
    menu = getmenu()
    nax_menu = [inquirer.Checkbox(
        "nax_menu",
        message='Please select option',
        choices=menu,
    )]
    nax = inquirer.prompt(nax_menu,theme=GreenPassion())
    for i in nax['nax_menu'] :
        start_action(i)


if __name__ == '__main__':
    clear()
    _modnax()
    time.sleep(config.wait_close)