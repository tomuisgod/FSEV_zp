print("Zadaj mená postupne po jednom: ")
zoznam_mien = []
filter_mien = []

while True:
    try:
        mena = input("")
        if mena == "":
            print("ERROR: Nezadali ste ziadne meno")
            break
        if "," in mena or " " in mena:
            raise ValueError("Zadajte iba jedno meno naraz, nie viac")

        zoznam_mien.append(mena)
    except ValueError as e:
        print(e)

    znova = input("\nChcete pridat dalsie meno? (ano/nie)").strip().lower()
    if znova != "ano":
        break

for n in zoznam_mien:
    if len(n) > 4:
        filter_mien.append(n)

print("Nevyfiltovany zoznam: \n", zoznam_mien)
print("Vyfiltrovany zoznam: \n", filter_mien)

