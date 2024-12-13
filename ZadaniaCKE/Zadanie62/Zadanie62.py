lista_liczb1 = []
with open("liczby1.txt", "r") as plik:
    for linia in plik.readlines():
        lista_liczb1.append(linia.strip())

def PierwszeZadanie():
    max_d = 0
    min_d = int(lista_liczb1[0].strip())

    max_o = ''
    min_o = ''

    for i in lista_liczb1:
        orginal = i
        W = int(i[0])
        for j in i[1:]:
            W = W * 8 + int(j)

        if W > max_d:
            max_d = W
            max_o = orginal

        if W < min_d:
            min_d = W
            min_o = orginal

    return max_d, min_d, max_o, min_o

print(PierwszeZadanie())

