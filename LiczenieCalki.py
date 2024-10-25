#Metoda z prostokątami
def f(x):
    return x*x + 1

def obliczenie():
    a = 0
    b = 4
    E = 1000
    y = 0

    x = (b - a) / E

    for i in range(E):
        y += f(a + i * x) * x
    return y
print(obliczenie())