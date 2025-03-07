with open('tekst.txt', 'r') as plik:
    tekst = plik.readline()
print(tekst)

#Zadanie 73.1
lista_napisow = tekst.split()

licznik = 0
for napis in lista_napisow:
    for i in range(len(napis) - 1):
        if napis[i] == napis[i+1]:
            licznik += 1
            break
print(licznik)

#Zadanie 73.2
litery = {}
for znak in tekst:
    if znak != " " and znak != "\n":
        if znak in litery:
            litery[znak] += 1
        else:
            litery[znak] = 1

suma = 0
for v in litery.values():
    suma += v

litery['Z'] = 0
for i in range(26):
    print(chr(i+65), ':', litery[chr(i+65)], round(litery[chr(i+65)]/suma*100, 2), "%")

#73.3
samogloski = ['A', 'E', 'I', 'O', 'U', 'Y']
ilosc_slow = 0
maks = 0

for napis in lista_napisow:
    n = 0
    for i in range(len(napis)):
        if napis[i] not in samogloski:
            n+=1
            if n == maks:
                ilosc_slow += 1
            if n > maks:
                maks = n
                ilosc_slow = 1
        else:
            n = 0

print(maks, ilosc_slow)