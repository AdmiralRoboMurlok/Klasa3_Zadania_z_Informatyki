import  math

lista = []
with open("liczby.txt", "r") as plik:
    for linia in plik.readlines():
        lista.append(int(linia))

licznik = 0
l1 = 0
l2 = 0

for i in lista:
    if i < 1000:
        licznik += 1
        l1=l2
        l2=i

print(licznik, l1, l2)


for n in lista:
    lista_dzielniki = []
    dzielniki = 0
    for m in range(1, n + 1):
        if n % m == 0:
            dzielniki += 1
            lista_dzielniki.append(m)
    if dzielniki == 18:
        print(n)
        print(lista_dzielniki)


