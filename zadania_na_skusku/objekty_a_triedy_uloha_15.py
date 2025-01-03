import math


class Kruh:
    def __init__(self, polomer):
        self.polomer = float(polomer)

    def obvod(self):
        return 2 * math.pi * self.polomer

    def plocha(self):
        return math.pi * self.polomer ** 2


zoznam_kruhov = [Kruh(10), Kruh(5)]
n = 1
for k in zoznam_kruhov:
    print(f"Polomer {n}. kruhu: {k.polomer}")
    print(f"Obvod {n}. kruhu: {k.obvod():.2f}")
    print(f"Plohca {n}. kruhu: {k.plocha():.2f}")
    print("_________________________________")
    n += 1
