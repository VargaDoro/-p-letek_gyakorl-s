'''1.feladat'''

def elso():
    nev:str=str(input("Adja meg a játékos nevét: "))
    szerep:str=str(input("Adja meg a játékos szerepkörét: "))

    print(f"Játékos neve: {nev}")
    print(f"szerepkör: {szerep}")

    if szerep=="varázsló":
        elet:int=2
    elif szerep=="harcos":
        elet:int=10
    else:
        elet:int=8

    print(f"Üdvözlünk {nev}, {elet} életed van!")
