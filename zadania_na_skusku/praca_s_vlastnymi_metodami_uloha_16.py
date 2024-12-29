class Student:
    def __init__(self, meno, priezvisko, znamky):
        self.meno = meno
        self.priezvisko = priezvisko
        self.znamky = znamky

    def priemer_znamok(self):
        if not self.znamky:
            return 0.0
        else:
            return sum(self.znamky) / len(self.znamky)

    def slovne_hodnotenie(self):
        priemer = self.priemer_znamok()
        if priemer <= 1.5:
            return "Vyborny"
        elif priemer <= 2.5:
            return "Chvalitebny"
        elif priemer <= 3.5:
            return "Dobry"
        elif priemer <= 4.5:
            return "Dostatocny"
        else:
            return "Nedostatocny"


Zoznam_studentov = [Student("Jozko", "Mrkvicka", [1, 2, 5, 3, 1]),
                    Student("Alzbetka", "Pacanova", [1, 1, 2, 1, 1]),
                    Student("Marek", "Mlady", [3, 4, 2, 5, 4]),
                    Student("Katka", "Macikova", [2, 2, 3, 1, 2])]

n = 1
for student in Zoznam_studentov:
    print(f"{n}. {student.meno} {student.priezvisko} -- Priemer: {student.priemer_znamok():.2f} ; Slovne hodnotenie: {student.slovne_hodnotenie()}")
    n += 1
