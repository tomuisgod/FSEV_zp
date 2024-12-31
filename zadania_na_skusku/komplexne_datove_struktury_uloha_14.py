print("Zadaj meno a vek osoby vo formate 'Meno : vek'")
osoby = {}
while True:
    osoba = input("")
    try:
        meno, vek = osoba.rsplit(" : ", 1)
        osoby[meno] = int(vek)
    except ValueError:
        print("ERROR: Neplatny format, pouzi format 'Meno : vek'")
        continue

    znova = input("\nChcete pridat dalsi produkt? (ano/nie): ").strip().lower()
    if znova != "ano":
        break


def bubblesort(osoby_dic):
    policko = list(osoby_dic.items())
    for i in range(len(policko) - 1):
        for j in range(len(policko) - 1 - i):
            if policko[j][1] > policko[j + 1][1]:
                policko[j], policko[j + 1] = policko[j + 1], policko[j]
    return policko

zoradene_osoby = bubblesort(osoby)
print("Zoznam zadanych osob:")
for meno, vek in zoradene_osoby:
    print(f"{meno} : {vek}")

print("Najstarsia osoba:", max(osoby, key=osoby.get))
print("Najmladsia osoba:", min(osoby, key=osoby.get))

