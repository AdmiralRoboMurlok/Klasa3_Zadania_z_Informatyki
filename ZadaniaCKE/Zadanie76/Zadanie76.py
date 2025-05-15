#76.1
lista = []
klucz = []
with open("szyfr1.txt") as plik:
    for i in range(6):
        lista.append(plik.readline().strip())
    klucz=plik.readline().split()

print(lista)

def szyfruj76(slowo, klucz):
    lista_liter = []
    for litera in slowo:
        lista_liter.append(litera)

    for n in range(len(lista_liter)):
        tmp = lista_liter[n]
        lista_liter[n] = lista_liter[(klucz[n % len(klucz)] - 1)]
        lista_liter[(klucz[n % len(klucz)] - 1)] = tmp

    slowo = ""
    for m in lista_liter:
        slowo += m
    return  slowo

#przykład
slowo = "INFORMATYKA"
klucz2 = [3, 2, 5, 4, 1]

print(szyfruj76(slowo, klucz2))

klucz_fix = []
for liczba in klucz:
    klucz_fix.append(int(liczba))

for linia in lista:
    print(szyfruj76(linia, klucz_fix))

#76.2
lista = []
klucz = []
with open("szyfr2.txt") as plik:
    lista.append(plik.readline().strip())
    klucz=plik.readline().split()

klucz_fix = []
for liczba in klucz:
    klucz_fix.append(int(liczba))

for linia in lista:
    print(szyfruj76(linia, klucz_fix))

#76.3
