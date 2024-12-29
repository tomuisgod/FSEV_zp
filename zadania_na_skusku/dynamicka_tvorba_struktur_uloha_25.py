def menu():
    produkty = {}
    while True:
        print("1. Zadaj cenu a produkty\n2. Zobraz produkty\n3. Pridat produkt\n4. Uprav cenu\n5. Odstran produkt\n6. Koniec")
        volba = int(input("Vyber si operaciu: "))
        if volba == 1:
            loading_produktov(produkty)
        elif volba == 2:
            zobraz_produkty(produkty)
        elif volba == 3:
            pridaj_produkt(produkty)
        elif volba == 4:
            uprav_produkt(produkty)
        elif volba == 5:
            vymaz_produkt(produkty)
        elif volba == 6:
            break
        else:
            print("ERROR: Moznost neexistuje, prosim zopakuj vyber")


def loading_produktov(produkty):
    print("Zadaj produkty s cenou vo formate 'Nazov produktu : Cena'")
    while True:
        produkt = input("Zadaj produkt: ")
        try:
            nazov_produktu, cena = produkt.rsplit(' : ', 1)
            produkty[nazov_produktu] = float(cena)
        except ValueError:
            print("ERROR: Neplatny format, pouzi format 'Nazov produktu : Cena'")
            continue

        znova = input("\nChcete pridat dalsi produkt? (ano/nie): ").strip().lower()
        if znova != "ano":
            break


def zobraz_produkty(produkty):
    print("\n")
    print("Zoznam produktov")
    if not produkty:
        print("ERROR: Slovnik produktov je prazdny. Pridaj produkty pre zobrazenie slovnika")
    else:
        n = 1
        for nazov_produktu, cena in produkty.items():
            print(f"{n}. {nazov_produktu} : {cena} $")
            n += 1
    print("\n")

def pridaj_produkt(produkty):
    while True:
        produkt = input("Zadaj produkty s cenou vo formate 'Nazov produktu : Cena'\n")
        if produkt in produkty:
            print("ERROR: Produkt uz existuje")
        else:
            try:
                nazov_produktu, cena = produkt.rsplit(" : ", 1)
                produkty[nazov_produktu] = float(cena)
                break
            except ValueError:
                print("ERROR: Neplatny format, pouzi format 'Nazov produktu : Cena'")
                continue

def uprav_produkt(produkty):
    produkt = input("Zadaj nazov produktu: ")
    if produkt in produkty:
        try:
            print(f"Vybral si si produkt {produkt} : {produkty[produkt]} $")
            cena = float(input("Zadaj novu cenu produktu: "))
            produkty[produkt] = cena
            print(f"Cena produktu {produkt} bola zmenena na {cena} $")
        except ValueError:
            print("ERROR: Nezadal si cislo")
    else:
        print("ERROR: Produkt, ktory si si vybral neexistuje")

def vymaz_produkt(produkty):
    produkt = input("Zadaj nazov produktu: ")
    if produkt in produkty:
        del produkty[produkt]
        print(f"Produkt {produkt} bol uspesne vymazany zo slovnika")
    else:
        print("ERROR: Produkt neexistuje")

menu()
