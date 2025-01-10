def nwd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


liczniki = []
mianowniki = []
with open("dane_ulamki.txt", "r") as plik:
    for linia in plik.readlines():
        liczby = linia.split()
        liczniki.append(int(liczby[0]))
        mianowniki.append(int(liczby[1]))
print(liczniki)
print(mianowniki)

minimalny_ulamek = [liczniki[0], mianowniki[0]]
for i in range(len(liczniki)):
    liczba = liczniki[i]/mianowniki[i]
    if liczba == minimalny_ulamek[0]/minimalny_ulamek[1]:
        if liczniki[i] < minimalny_ulamek[0]:
            minimalny_ulamek[0] = liczniki[i]
            minimalny_ulamek[i] = mianowniki[i]
    elif liczba < minimalny_ulamek[0] / minimalny_ulamek[1]:
        minimalny_ulamek[0] = liczniki[i]
        minimalny_ulamek[1] = mianowniki[i]
print(minimalny_ulamek)

ilosc = 0
for i in range(len(liczniki)):
    if nwd(liczniki[i], mianowniki[i]) == 1:
        ilosc += 1
print(ilosc)


suma_licznikow = 0
for i in range(len(liczniki)):
    licznik = liczniki[i]
    mianownik = mianowniki[i]
    while nwd(licznik, mianownik) != 1:
        nwdd = nwd(licznik, mianownik)
        licznik = licznik // nwdd
        mianownik = mianownik // nwdd
    suma_licznikow += licznik
print(suma_licznikow)