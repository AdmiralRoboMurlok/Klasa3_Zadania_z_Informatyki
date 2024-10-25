P = int(input())

def absoulute(n):
    if n < 0:
        n = n * -1
    return n

def Pierw(P):
    E = 0.0001  # przybliżenie

    a = 1  # bok 1
    b = P  # bok 2
    while absoulute(a - b) > E:
        a = (a + b) / 2
        b = P/a

    return a

print(Pierw(P))