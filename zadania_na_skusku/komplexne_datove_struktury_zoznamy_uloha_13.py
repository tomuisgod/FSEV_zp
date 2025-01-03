print("Zadaj cislo, ktore chces pridat do zoznamu (po jednom)")

zoznam_cisel = []

while True:
    try:
        cislo = float(input(""))
        zoznam_cisel.append(cislo)
        cislo = 0
    except ValueError as e:
        print(f"ERROR: Input nie je cislo\n{e}")
        continue

    znova = input("Chces zadat dalsie cislo? (ano/nie): ")
    if znova != "ano":
        break

def bubblesort(policko):
    for i in range(len(policko)):
        for j in range(len(policko)):
            if policko[i] > policko[j]:
                policko[i], policko[j] = policko[j], policko[i]
    return policko


print(zoznam_cisel)
print(bubblesort(zoznam_cisel))
print(f"Najvacsie cislo: {max(zoznam_cisel)}")
print(f"Najmensie cislo: {min(zoznam_cisel)}")