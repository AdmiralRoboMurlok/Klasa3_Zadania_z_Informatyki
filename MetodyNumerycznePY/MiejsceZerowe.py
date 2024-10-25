def f(x):
    return x*2 - 2

def MiejsceZerowe(a, b):
    E = 0.0001
    s = 0
    if f(a) * f(b) <= 0:
        while abs(a - b) > E:
            s = (a + b) / 2
            if f(a) * f(s) <= 0:
                b = s
            else:
                a = s

    return s


a = int(input())
b = int(input())

print(MiejsceZerowe(a, b))