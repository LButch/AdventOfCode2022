import numpy as np

with open("Tag9.txt") as f:
    raw = f.read().split("\n")
    raw = [i.split(" ") for i in raw]
    raw = [[i[0],int(i[1])] for i in raw]

def visuPositionen(diePositionen,zeichen="#"):
    x = []
    y = []
    for xx,yy in diePositionen:
        x.append(xx)
        y.append(yy)

    offX = min(x) * (-1)
    x = max(x) + offX + 1
    offY = min(y) * (-1)
    y = max(y) + offY + 1

    print(x,y)
    print(offX,offY)

    matrix = np.zeros((x,y))
    for xx, yy in diePositionen:
        matrix[xx + offX][yy + offY] = 1

    matrix = np.rot90(matrix)

    print(str(matrix).replace("1",zeichen))
    return np.sum(matrix)

positionenHead = [(0,0)]    # Positionsverlauf mit Startposition
aktuellePosition = [0,0] # x,y

for richtung,menge in raw:
    for bla in range(menge):
        if richtung == "U":
            aktuellePosition[0] += 1
        if richtung == "D":
            aktuellePosition[0] -= 1
        if richtung == "R":
            aktuellePosition[1] += 1
        if richtung == "L":
            aktuellePosition[1] -= 1

        positionenHead.append(tuple(aktuellePosition))

print(positionenHead)
visuPositionen(positionenHead,"H")

def bewegeHin(jetzt,soll):
    if jetzt == soll:
        return jetzt
    if jetzt < soll:
        return jetzt + 1
    return jetzt - 1

px,py = (0,0)
positionenTail = [(0,0)]

diff = lambda a,b:abs(a - b)

for hx,hy in positionenHead:

    if diff(hx,px) < 2 and diff(hy,py) < 2:
        continue

    if diff(hx,px) == 2 or diff(hy,py) == 2:
        px = bewegeHin(px,hx)
        py = bewegeHin(py,hy)


    positionenTail.append((px,py))

print(visuPositionen(positionenTail))


