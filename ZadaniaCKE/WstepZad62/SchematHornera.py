#Schemat Hornera zmienia system zapisu liczby na wielomian
#Nie działa na sytemach z literami
# 11010 = 1 * 2^4 + 1 * 2^3 + 0 * 2^2 + 1 * 2^1 * 0 * 2^0
# --||-- = 1 * x^4 + 1 * x^3 + 0 * x^2 + 1 * x^1 * 0 * x^0
# --||-- = a0 * x^4 + a1 * x^3 + a2 * x^2 + a3 * x^1 * a4 * x^0

# W0 = a0
# Wn = W n-1 * x + a n

# W0 = 1
# W1 = 1 * 2 + 1 = 3
# W2 = 3 * 2 + 0 = 6
# W3 = 6 * 2 + 1 = 13
# W4 = 13 * 2 + 0 = 26

#Gdzie liczba to string a x to integer
#liczba x to system na z którego zmieniamy
def horner(liczba, x):
    W = int(liczba[0])
    for i in liczba[1:]:
        W = W * x + int(i)

    return W

print(horner("11010", 2))


#Zmiana liczby z systemu 10 na inny
#liczba to int, x to int
#x to sytem
def DecToAll(liczba, x):
    wynik = ""
    while liczba > 0:
        wynik = str(liczba%x) + wynik
        liczba = liczba // x

    return wynik

print(DecToAll(26, 2))