def szyfruj(tekst, A, B):
    szyfr = ""
    for litera in tekst:
        numer = ord(litera) - 97
        numer = numer * A
        numer = numer + B
        numer = numer % 26

        szyfr += chr(numer + 97)
    return szyfr

with open("tekst.txt") as plik:
    tekst = plik.readline()

lista = tekst.split()

#75.1
for wyraz in lista:
    if wyraz[0] == 'd' and wyraz[-1] == 'd':
        print(wyraz)

#75.2
for wyraz in lista:
    if len(wyraz) >= 10:
        print(szyfruj(wyraz, 5, 2))

#75.3
with open("probka.txt") as plik:
    for linia in plik:
        wyrazy = linia.split()
        for a in range(26):
            for b in range(26):
                if szyfruj(wyrazy[0], a, b) == wyrazy[1]:
                    print(wyrazy, a, b)
                    break
        for a in range(26):
            for b in range(26):
                if szyfruj(wyrazy[1], a, b) == wyrazy[0]:
                    print(wyrazy, a, b)
                    break