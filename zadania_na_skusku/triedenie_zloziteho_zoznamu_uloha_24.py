og_slovnik = {}

print("Zadaj meno a vek vo formate 'Meno : vek'")
while True:
    osoby = input("")
    try:
        meno, vek = osoby.rsplit(" : ", 1)
        og_slovnik[meno] = int(vek)
    except ValueError:
        print("ERROR: Neplatny format, pouzi format 'Meno : vek'")
        continue
    znova = input("Chcete pridat dalsiu osobu? (ano/nie)").strip().lower()
    if znova != "ano":
        break

zoznam_osob = []
for meno, vek in og_slovnik.items():
    osoba = {"meno": meno, "vek": vek}
    zoznam_osob.append(osoba)

print("Originalny zoznam osob")
for osoba in zoznam_osob:
    print(osoba)

sorted_slovnik = sorted(zoznam_osob, key=lambda osoba: (osoba["vek"], osoba["meno"]))

print("Zoradeny zoznam osob")
for osoba in sorted_slovnik:
    print(osoba)

