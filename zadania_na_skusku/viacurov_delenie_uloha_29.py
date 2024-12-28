class Zviera:
    def __init__(self, meno="NON", vek=0):
        self.meno = meno
        self.vek = vek

    def info(self):
        print(f"Zviera: {self.meno}, Vek: {self.vek}")

class Cicavec(Zviera):
    def __init__(self, meno="NON", vek=0, sposob_pohybu="NON"):
        super().__init__(meno, vek)
        self.sposob_pohybu = sposob_pohybu

    def info(self):
        print(f"Cicavec: {self.meno}, Vek: {self.vek}, Sposob pohybu: {self.sposob_pohybu}")

class Pes(Cicavec):
    def __init__(self, meno="NON", vek=0, sposob_pohybu="Bezanie"):
        super().__init__(meno, vek, sposob_pohybu)

    def stekaj(self):
        print(f"Pes {self.meno} steka hav hav")

zviera = Zviera("Slon", 10)
zviera.info()

cicavec = Cicavec("Macka", 3, "Bezanie")
cicavec.info()

pes = Pes("Rex", 2)
pes.info()
pes.stekaj()
