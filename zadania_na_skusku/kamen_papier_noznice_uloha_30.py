import random

class KPN:
    def __init__(self, skore_pc=0, skore_clovek=0):
        self.skore_pc = skore_pc
        self.skore_clovek = skore_clovek


    def zobraz_skore(self):
        print(f"Aktualne skore je:\nClovek: {self.skore_clovek}\nPC: {self.skore_pc}")

    def pridaj_clovek(self):
        self.skore_clovek += 1

    def pridaj_pc(self):
        self.skore_pc += 1


def kpp_hra():
    kpn = KPN()
    moznosti = {"k": "kamen", "p": "papier", "n": "noznice"}
    while True:
        print("K: Kamen\nP: Papier\nN: Noznice\nQ: Koniec")
        volba = str(input("Vyber si moznost: ")).strip().lower()

        if volba == "q":
            break
        if volba not in moznosti:
            print("ERROR: Neexistujuca volba, opakujte vyber")

        pc_volba = random.choice(list(moznosti.keys()))

        print(f"Tvoja volba: {moznosti[volba]}")
        print(f"PC volba: {moznosti[pc_volba]}")

        if volba == pc_volba:
            print("Remiza")
        elif (volba == "k" and pc_volba == "n") or \
                (volba == "p" and pc_volba == "k") or \
                (volba == "n" and pc_volba == "p"):
            print("Vyhral si")
            kpn.pridaj_clovek()
        else:
            print("Prehral si")
            kpn.pridaj_pc()
        kpn.zobraz_skore()


kpp_hra()