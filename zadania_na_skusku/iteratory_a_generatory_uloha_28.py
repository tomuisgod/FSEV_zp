cisla = []
a, b = 0, 1
while a <= 10000:
    cisla.append(a)
    a, b = b, a + b

print(cisla)