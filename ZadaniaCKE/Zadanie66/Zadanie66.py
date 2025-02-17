lista_trojek = []

with open("trojki.txt", 'r') as plik:
    for linia in plik:
        lista_trojek.append(linia.split())

print("66.1") #66.1
def suma_cyfr(liczba): # Sumuje pojedyńcze cyfry liczby
    suma = 0
    for i in liczba:
        suma += int(i)
    return suma

for lista in lista_trojek:
    if (suma_cyfr(lista[0])+suma_cyfr(lista[1])) == int(lista[2]):
        print(lista)

print("66.2")#66.2
def pierw(a): # Obliczanie czy liczba jest pierwsza
    for i in range(2, a//2):
        if a % i == 0:
            return False
    return True

for lista_pierw in lista_trojek:
    if pierw(int(lista_pierw[0])) and pierw(int(lista_pierw[1])):
        if int(lista_pierw[0]) * int(lista_pierw[1]) == int(lista_pierw[2]):
            print(lista_pierw)

print("66.3") #66.3 poprawić musi być para wierszy
def trojkat(boka, bokb, bokc): # Sprawdzanie czy z liczb można stworzyć trokąt prostokątny
    return (boka*boka) + (bokb*bokb) == bokc*bokc

poprzednik = False
poprzednik_liczba = 0
lista_popraw = []

for lista_pot in lista_trojek:
    teraz = trojkat(int(lista_pot[0]), int(lista_pot[1]), int(lista_pot[2])) or trojkat(int(lista_pot[0]), int(lista_pot[2]), int(lista_pot[1])) or trojkat(int(lista_pot[2]), int(lista_pot[1]), int(lista_pot[0]))
    if poprzednik and teraz:
        if poprzednik not in lista_popraw:
            lista_popraw.append(poprzednik_liczba)
        lista_popraw.append(lista_pot)

    poprzednik = teraz
    if poprzednik == False and teraz == False:
        poprzednik_liczba = 0
    elif teraz == True:
        poprzednik_liczba = lista_pot

print(lista_popraw)