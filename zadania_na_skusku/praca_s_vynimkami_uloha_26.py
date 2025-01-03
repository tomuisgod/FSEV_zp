while True:
    try:
        cislo1 = float(input("Zadaj číslo 1: "))
        cislo2 = float(input("Zadaj číslo 2: "))

        vysledok = cislo1 / cislo2

    except ZeroDivisionError:
        print("ERROR: Delenie nulou nie je mozne")
        continue
    except ValueError:
        print("ERROR: Zadane cislo nie je platne")
    else:
        print(f"Vysledok delenia cisel {cislo1} a {cislo2} je {vysledok}")

    znova = input("Chcete pokracovat znova? (ano/nie) \n").strip().lower()
    if znova != "ano":
        break

