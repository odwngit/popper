import os
import json
from rich.pretty import pprint
from rich import print as richprint
github_link = "https://www.github.com/odwngit/popper"
funko_data = json.load(open(r'funko_pop.json', encoding="utf8"))
os.system("title popper")
os.system("cls")
while True:
    returned = 0
    richprint(f"[cyan bold]popper [italic link={github_link}]github[/italic link][/cyan bold]")
    richprint("[green]buy me a bubble tea [link=https://buymeacoffee.com/odwn]here[/link][/green]")
    richprint("[yellow italic]enter your search type (series or name)[/yellow italic]")
    searchtype = input("- ")
    richprint("[yellow italic]enter your funko search[/yellow italic]")
    search = input("- ")
    for fig in funko_data:
        if searchtype == "name":
            if search in fig["handle"] or search in fig["title"]:
                richprint(f"[blue]found! [/blue]{fig['title']}, [link={fig['imageName']}]image[/link]")
                returned += 1
        elif searchtype == "series":
            for tag in fig["series"]:
                if search in tag:
                    richprint(f"[blue]found! [/blue]{fig['title']}, [link={fig['imageName']}]image[/link]")
                    returned += 1
    richprint(f"[pink]returned [white]{returned}[/white] results[/pink]")
    richprint("[red]press [underline]enter[/underline] to go to new search[/red]")
    input("")
    os.system("cls")
