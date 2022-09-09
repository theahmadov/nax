import inquirer
import json
from inquirer.themes import *
from colorama import Fore 
from modnax.lib.load import *

class conf:
    database = "./modnax/database/nax_db.json"
    menu = ["database","user_list","token_list","spesific",">>"]


############################
#        Read JSON NAME    #
############################

def unfo(name):
    with open(conf.database, 'r') as user_config:
        user_db = user_config.read()
        database = json.loads(user_db)
    try:
        return database["user"][name]
    except:
        pass 


############################
#        Read JSON Token   #
############################

def utoken(token):
    with open(conf.database, 'r') as user_config:
        user_db = user_config.read()
        database = json.loads(user_db)
    try:
        return database["token"][token]
    except:
        pass 


############################
#        Read Json FULL    #
############################

def read_nax():
    with open(conf.database, 'r') as user_config:
        user_db = user_config.read()
        database = json.loads(user_db)
    try:
        return database
    except:
        pass 


############################
#        Getnames          #
############################

def getnames():
    with open(conf.database, 'r') as user_config:
        user_db = user_config.read()
        database = json.loads(user_db)
    try:
        return database["names"]
    except:
        pass 

############################
#        User_Lst          #
############################

def nax_db_user():
    
    from rich.tree import Tree
    from rich import print as rprint
    from rich.console import Console

    tree = Tree("[blue]nax")
    cnt = 1
    for i in read_nax()["names"]:
        
        if(read_nax()["user"][i]["color"]=="red"):
            tree.add(f"{cnt} : [red]{i}")
        elif(read_nax()["user"][i]["color"]=="blue"):
            tree.add(f"{cnt} : [blue]{i}")
        elif(read_nax()["user"][i]["color"]=="cyan"):
            tree.add(f"{cnt} : [cyan]{i}")
        elif(read_nax()["user"][i]["color"]=="green"):
            tree.add(f"{cnt} : [green]{i}")
        elif(read_nax()["user"][i]["color"]=="yellow"):
            tree.add(f"{cnt} : [yellow]{i}")
        cnt+=1
    rprint(tree)
############################
#        Token_Lst         #
############################

def nax_db_token():
    from rich.tree import Tree
    from rich import print as rprint
    from rich.console import Console
    cnt=1
    
    tree = Tree("[blue]nax")

    for i in read_nax()["names"]:
        if(read_nax()["user"][i]["color"]=="red"):
            tree.add(f"{cnt} : [red]{read_nax()['user'][i]['token']}")
        elif(read_nax()["user"][i]["color"]=="blue"):
            tree.add(f"{cnt} : [blue]{read_nax()['user'][i]['token']}")
        elif(read_nax()["user"][i]["color"]=="cyan"):
            tree.add(f"{cnt} : [cyan]{read_nax()['user'][i]['token']}")
        elif(read_nax()["user"][i]["color"]=="green"):
            tree.add(f"{cnt} : [green]{read_nax()['user'][i]['token']}")
        elif(read_nax()["user"][i]["color"]=="yellow"):
            tree.add(f"{cnt} : [yellow]{read_nax()['user'][i]['token']}")
        
        cnt+=1
    rprint(tree)

############################
#        Spesific          #
############################

def nax_db_spesific():  
    
    usernames = getnames()
    nax_db_spesific = [inquirer.Checkbox(
        'nax_user',
        message="Please select option",
        choices=usernames,
    )]
    nax = inquirer.prompt(nax_db_spesific,theme=GreenPassion())
    from prettytable import PrettyTable
    nax_data = PrettyTable(["user", "role", "color", "banned", "token"])
    for i in nax['nax_user'] :
        nax_data.add_row([i,read_nax()["user"][i]["role"],read_nax()["user"][i]["color"],read_nax()["user"][i]["banned"],read_nax()["user"][i]["token"]])
    print(nax_data)


############################
#        Database          #
############################
def nax_db_database():
    from prettytable import PrettyTable
    load_data(read_nax()["names"])
    nax_data = PrettyTable(["username", "role", "color", "banned", "token"])
    for i in range(0,read_nax()["count"]):
        nax_data.add_row([read_nax()["names"][i],
        read_nax()["user"][read_nax()["names"][i]]["role"], 
        read_nax()["user"][read_nax()["names"][i]]["color"], 
        read_nax()["user"][read_nax()["names"][i]]["banned"],
        read_nax()["user"][read_nax()["names"][i]]["token"]])
    
    print(nax_data)



############################
#        Menu              #
############################
def nax_db_menu():
    menu = conf.menu
    nax_menu = [inquirer.Checkbox(
        'nax_menu',
        message="Please select option",
        choices=menu,
    )]
    nax = inquirer.prompt(nax_menu,theme=GreenPassion())
    for i in nax['nax_menu']:
        if(i=="spesific"):
            nax_db_spesific()
        elif(i=="database"):
            nax_db_database()
        elif(i=="user_list"):
            nax_db_user()
        elif(i=="token_list"):
            nax_db_token()
