class Bankovy_ucet:
    def __init__(self, cislo_uctu, zostatok):
        self.cislo_uctu = cislo_uctu
        self.zostatok = float(zostatok)

    def vypis_uctu(self):
        print(f"{self.cislo_uctu} : {self.zostatok} $")

    def vklad_penazi(self):
        vklad = float(input("Zadaj sumu na vloženie: "))
        self.zostatok += vklad
        print(f"Na ucet {self.cislo_uctu} bola pridaná suma {vklad} $\nNový zostatok je: {self.zostatok} $")

    def vyber_penazi(self):
        vyber = float(input("Zadaj sumu ma výber: "))
        while self.zostatok < vyber:
            print("ERROR: Nedostatocne financne prostriedky na ucte. Zopakuje prosim operaciu znova")
            vyber = float(input("Zadaj sumu na výber: "))
        self.zostatok -= vyber
        print(f"Z uctu {self.cislo_uctu} bola vybrana suma {vyber} $.\nNovy zostatok je: {self.zostatok} $")


bankove_ucty = [Bankovy_ucet("4567898765678987656", "10")]

def menu():
    while True:
        print("\n1. Zobrazenie zostatku\n2. Vklad penazi\n3. Vyber penazi\n4. Ukoncenie programu")
        try:
            volba = int(input("Vyberte si operaciu: "))
        except ValueError:
            print("ERROR: Neexistujuca volba, opakujte vyber")
            continue

        if volba == 1:
            ucet = bankove_ucty[0]
            ucet.vypis_uctu()
        elif volba == 2:
            ucet = bankove_ucty[0]
            ucet.vklad_penazi()
        elif volba == 3:
            ucet = bankove_ucty[0]
            ucet.vyber_penazi()
        elif volba == 4:
            break
        else:
            print("ERROR: Neexistujuca volba, opakujte vyber")
            continue

        # Možnosť zopakovania alebo ukončenia
        znova = input("\nChcete vykonať ďalšiu operáciu? (ano/nie): ").strip().lower()
        if znova != "ano":
            break

menu()
