from datetime import datetime

akt_cas = datetime.now()
print(f"Aktuálny čas je: {akt_cas.strftime('%Y-%m-%d %H:%M:%S')}")

datum1 = input("Zadaj prvý dátum vo formáte (YYYY-MM-DD): ")
datum2 = input("Zadaj druhý dátum vo formáte (YYYY-MM-DD): ")

try:
    d1 = datetime.strptime(datum1, "%Y-%m-%d")
    d2 = datetime.strptime(datum2, "%Y-%m-%d")
    delta = abs(d2 - d1)

    d = delta.days
    t_s = delta.total_seconds() - d * 86400
    h, z = divmod(t_s, 3600)
    m = z // 60

    print(f"Rozdiel medzi dátumami {datum1} a {datum2}")
    print(f"Dni: {d}, Hodiny: {int(h)}, Minuty: {int(m)}")


except ValueError:
    print("ERROR: Nesprávne zadaný dátum. Pouzite format (YYYY-MM-DD)")


