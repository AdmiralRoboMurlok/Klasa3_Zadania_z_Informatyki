lista_napis = []
with open("napisy.txt", "r") as plik:
    for linia in plik:
        lista_napis.append(linia.split())

#72.1
licznik = 0
for napisy in lista_napis:
    if len(napisy[0]) >= 3 * len(napisy[1]) or len(napisy[1]) >= 3 * len(napisy[0]):
        if licznik < 1:
            print(napisy)
        licznik += 1
print(licznik)

#72.2
for napisy in lista_napis:
    if napisy[1][:len(napisy[0])] == napisy[0]:
        print(napisy)

#72.3
def ile_liter_od_prawej(napis1, napis2):
    n = 0
    if len(napis1) > len(napis2):
        for i in range(len(napis2)):
            if napis2[-1-i] == napis1[-1-i]:
                n += 1
            else:
                return n
    else:
        for i in range(len(napis1)):
            if napis2[-1-i] == napis1[-1-i]:
                n += 1
            else:
                return n

maks = 0
lista = []
for napisy in lista_napis:
    k = ile_liter_od_prawej(napisy[0], napisy[1])
    if k == maks:
        lista.append(napisy)
    if k > maks:
        maks = k
        lista = []
        lista.append(napisy)
print(maks, lista)