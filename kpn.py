import os
import time


class KPN:
    def __init__(self, skore_clovek1=0, skore_clovek2=0):
        self.skore_clovek1 = skore_clovek1
        self.skore_clovek2 = skore_clovek2

    def zobraz_skore(self):
        print(f"Aktualne skore je:\nHrac 1: {self.skore_clovek1}\nHrac 2: {self.skore_clovek2}")

    def pridaj_clovek1(self):
        self.skore_clovek1 += 1

    def pridaj_clovek2(self):
        self.skore_clovek2 += 1


# Funkcia na vyčistenie terminálu
clear = lambda: os.system("clear" if os.name == "posix" else "cls")


def kpp_hra():
    kpn = KPN()
    moznosti = {"k": "kamen", "p": "papier", "n": "noznice"}

    while True:
        print("K: Kamen\nP: Papier\nN: Noznice\nQ: Koniec")
        volba = str(input("Hrac 1: Vyber si moznost: ")).strip().lower()

        # Ak hráč 1 zadá 'q', hra sa ukončí
        if volba == "q":
            break
        if volba not in moznosti:
            print("ERROR: Neexistujuca volba, opakujte vyber")
            continue

        clear()  # Vyčistí obrazovku pred vstupom hráča 2

        volba_2 = str(input("Hrac 2: Vyber si moznost: ")).strip().lower()
        if volba_2 == "q":
            break
        if volba_2 not in moznosti:
            print("ERROR: Neexistujuca volba, opakujte vyber")
            continue

        clear()  # Vyčistí obrazovku pred vyhodnotením výsledkov

        print(f"Hrac 1 volba: {moznosti[volba]}")
        print(f"Hrac 2 volba: {moznosti[volba_2]}")

        if volba == volba_2:
            print("Remiza")
        elif (volba == "k" and volba_2 == "n") or \
                (volba == "p" and volba_2 == "k") or \
                (volba == "n" and volba_2 == "p"):
            print("Hrac 1 vyhral!")
            kpn.pridaj_clovek1()
        else:
            print("Hrac 2 vyhral!")
            kpn.pridaj_clovek2()

        kpn.zobraz_skore()
        time.sleep(5)  # Počká 5 sekúnd pred vymazaním obrazovky
        clear()


# Spustenie hry
kpp_hra()
