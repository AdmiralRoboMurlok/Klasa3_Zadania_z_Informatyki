def FuncF(x): # f(10) = 19 * 61 / 125
    R = (x*x*x*x) / 500 - (x*x) / 200 - 3 / 250
    return R

def FuncG(x): # g(10) = -32 * 2 / 3
    R = (x*x*x) / 30 + x / 20 + 1 / 6
    return R

def obliczenieCalki():
    TopY = 19 * (61 / 125)
    DownY = -32 * (2 / 3)
    LeftX = 2
    RightX = 10

    Height = TopY + DownY * -1
    Base = RightX - LeftX

    sumTop = 0
    sumDown = 0

    E = 1000

    # Początek 70.1
    var = (RightX - LeftX) / E

    for i in range(E):
        sumTop += FuncF(LeftX + i * var) * var

    for i in range(E):
        sumDown += FuncG(LeftX + i * var) * var

    sumFigure = sumTop + sumDown
    rectangle = Base * Height

    result = rectangle - sumFigure
    print(result)
    # Koniec 70.1

    # Początek 70.2


obliczenieCalki()