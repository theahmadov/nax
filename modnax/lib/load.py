from rich.progress import track
from time import sleep
from rich.console import Console


def process_data():
    sleep(0.02)

def load_bar(text):
    for _ in track(range(100), description=f'[green]{text}'):
        process_data()

def load_data(data):

    console = Console()

    with console.status("[bold green]Proccessing data...") as status:
        while data:
            num = data.pop(0)
            sleep(1)
            console.log(f"[green]Finished to load[/green] {num}")