lista_liczb1 = []
with open("liczby1.txt", "r") as plik:
    for linia in plik.readlines():
        lista_liczb1.append(linia.strip())

lista_liczb2 = []
with open("liczby2.txt", "r") as plik:
    for linia in plik.readlines():
        lista_liczb2.append(linia.strip())

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

def DrugieZadanie():
    start_max = 0
    ciag_max = 0
    poprzedni = 0

    ciag_teraz = 0
    start_teraz = lista_liczb2[0]
    for i in range(len(lista_liczb2)):
        if int(lista_liczb2[i]) >= poprzedni:
            ciag_teraz += 1
            poprzedni = int(lista_liczb2[i])
        else:
            if ciag_teraz > ciag_max:
                ciag_max = ciag_teraz
                start_max = lista_liczb2[i-ciag_teraz]

            ciag_teraz = 1
            start_teraz = lista_liczb2[i]
            poprzedni = int(lista_liczb2[i])

    if ciag_teraz > ciag_max:
        ciag_max = ciag_teraz
        start_max = start_teraz

    return start_max, ciag_max

print(DrugieZadanie())