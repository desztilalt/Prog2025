verseny_adatok = []

inputfajl = "F1-2024dec.csv"

def adat_beolvasas(fajl_nev):
    try:
        with open(fajl_nev, encoding="utf-8") as fajl:
            global verseny_adatok
            verseny_adatok = fajl.readlines()

    except Exception as ex:
        print(f"Halihóóóóó!: Hiba oka: {ex}")
    except FileNotFoundError:
        print("Hiba a fájl megnyitása közben!")


def pontatlanok():
    db = 0

    for i in range(1, len(verseny_adatok)):
        if(int(verseny_adatok[i].split(',')[1]) == 0):
            db = db + 1

    print(f"{db} versenyző nem szerzett még pontot.\n")

def versenyzo_kereses(nev):
    i = 0
    while (i<len(verseny_adatok)and nev not in verseny_adatok[i]):
        i=i+1
    if (i<len(verseny_adatok)):
        print("Van ilyen versenyző")
    else:
        print("Nincs ilyen versenyző")

def csapat(nev):
    i = 1
    while i < len(verseny_adatok) and nev not in verseny_adatok[i]:
        i = i + 1
    if i < len(verseny_adatok) and nev in verseny_adatok[i]:
        print("Van ilyen versenyző", verseny_adatok[i].split(',')[2].strip()," Csapatban van!")
    else:
        print("Nincs ilyen versenyző")


adat_beolvasas(inputfajl)
pontatlanok()
csapat("Pierre Gasly")

# Program

