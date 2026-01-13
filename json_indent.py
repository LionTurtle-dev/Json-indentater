##Json file indentater python script
import json

def indent(fl: str) -> None:
    v = None
    with open(fl, encoding='utf-8') as file:
        v = json.load(file)


    with open(fl, 'w', encoding='utf-8') as f:
        json.dump(v, f, indent=4)

while (fl := input('Add meg a Json file útvonalát! -> ')) != "":
    try:
        indent(fl)
    except json.decoder.JSONDecodeError:
        print(f'A(z) {fl} nem Json file!')
    except FileNotFoundError:
        print(f'A(z) „{fl}”, nevű file nem található!')
    else:
        print("Behúzás sikeres.")
        break
