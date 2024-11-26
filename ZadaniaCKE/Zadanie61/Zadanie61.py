ciagi = []
with open("ciagi.txt", "r") as plik:
    for linia in plik.readlines():
        liczby = []
        for liczba in linia.split():
            liczby.append(int(liczba))
        if len(liczby) > 1:
            ciagi.append(liczby)

print(len(ciagi), ciagi)

max = 0
licznik = 0

for ciag in ciagi:
    roznica = ciag[1] - ciag[0]
    for i in range(2, len(ciag)):
        if ciag[i] - ciag[i - 1] != roznica:
            break
    else:
        licznik += 1
        if roznica > max:
            max = roznica
print(licznik, max)

#print(27%(27**(1/3)))

#opcja 1 kinda brute force
for ciag in ciagi:
    for n in ciag:
        for p in range(1, 101):
            if p * p * p == n:
                print(n)

