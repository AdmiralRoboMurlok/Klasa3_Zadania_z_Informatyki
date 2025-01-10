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