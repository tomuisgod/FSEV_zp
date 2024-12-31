class Zamestnanec:
    def __init__(self, meno, plat):
        self.meno = meno
        self.plat = int(plat)

    def info(self):
        return f"Zamestnanec: {self.meno}, Plat: {self.plat}"

class Manazer(Zamestnanec):
    def __init__(self, meno, plat, oddelenie):
        super().__init__(meno, plat)
        self.oddelenie = oddelenie

    def info_man(self):
        return f"Zamestnanec: {self.meno}, Plat: {self.plat}, Oddelenie: {self.oddelenie}"

zamestnanec = Zamestnanec("Pavol Maron", 10000)
manazer = Manazer("Jozko Mrkvicka", 15000, "IT")

print(zamestnanec.info())
print(manazer.info_man())