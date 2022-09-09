from modnax.nax_db import *
from modnax.lib.mod_login import *
from modnax.nax_dash import *
from modnax.lib.load import *


def start_action(selection):
    if(selection == "nax_db"):
        nax_db_menu()
    elif(selection == "nax_dash"):
        nax_dash_menu()
