ciagi = []
with open("ciagi.txt", "r") as plik:
    for linia in plik.readlines():
        ciagi.append(linia.strip())
print(ciagi)

for i in range(len(ciagi)):
    if ciagi[i][:len(ciagi[i])//2] == ciagi[i][len(ciagi[i])//2:]:
        print(ciagi[i])

licznik = 0
for i in range(len(ciagi)):
    if "11" not in ciagi[i]:
        licznik += 1
print(licznik)


def horner(liczba, x):
    W = int(liczba[0])
    for i in liczba[1:]:
        W = W * x + int(i)

    return W

liczbyDz = []
for i in range(len(ciagi)):
    liczbyDz.append(horner(ciagi[i], 2))
print(liczbyDz)

#sito Eratostenesa
liczbyP = []
liczby = []
for i in range(270000):
    liczby.append(1)
for i in range(2, 270000):
    if liczby[i]==1:
        for j in range(i+i, 270000, i):
            liczby[j] = 0
for i in range(2, 270000):
    if liczby[i] == 1:
        liczbyP.append(i)

print(liczbyP)

for i in range(len(liczbyDz)):
    liczba = liczbyDz[i]
    czynniki = []
    for j in range(len(liczbyP)):
        while (liczba % liczbyP[j] == 0):
            czynniki.append(liczbyP[j])
            liczba = liczba//liczbyP[j]
        if len(czynniki) > 2:
            break
    if len(czynniki) == 2:
        print(liczbyDz[i], czynniki)