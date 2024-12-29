def calc_statistika(zamestnanci):
    pocet_z = len(zamestnanci)
    if pocet_z == 0:
        return {"pocet": 0, "priemerny_vek": 0, "priemerny_plat": 0}

    sum_plat = sum(zamestnanec_plat["plat"] for zamestnanec_plat in zamestnanci)
    sum_vek = sum(zamestnanec_vek["vek"] for zamestnanec_vek in zamestnanci)

    return {
        "pocet": pocet_z,
        "priemerny_vek": sum_vek / pocet_z,
        "priemerny_plat": sum_plat /pocet_z
    }


def txt_statistika(txt, stats):
    try:
       with open(txt, "x", encoding="utf-8") as f:
           print(f"Textovy subor {txt} bol vytvoreny")
    except FileExistsError:
        print(f"Textovy subor {txt} uz bol vytvoreny, zapisujem")
        pass
    with open(txt, "w", encoding="utf-8") as f:
        f.write(f"Počet zamestnancov: {stats['pocet']}\n")
        f.write(f"Priemerny vek: {stats['priemerny_vek']}\n")
        f.write(f"Priemerny plat: {stats['priemerny_plat']}\n")

def main():
    zamestnanci_txt = "zamestnanci.txt"
    statist = "statistika.txt"

    zamestnanci = []

    try:
        with open(zamestnanci_txt, "r", encoding="utf-8") as txt:
            for r in txt:
                meno, vek, plat = r.strip().split(",")
                zamestnanci.append({"meno": meno.strip(), "vek": int(vek), "plat": float(plat)})
    except FileNotFoundError:
        print("ERROR: Subor sa nenasiel alebo neexistuje")
        return
    except ValueError as e:
        print(f"ERROR: f{e}")
        return

    statistika = calc_statistika(zamestnanci)
    txt_statistika(statist, statistika)
    print("Statistika bola uspesne ulozena")

main()



