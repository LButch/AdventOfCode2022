
with open("Tag10.txt","r") as f:
    raw = f.read().split("\n")
    raw = [i.split(" ") for i in raw]

takte = []
aktuellesPixel = 0
x = 1

drawing = [[]]

def handlePixel():
    global aktuellesPixel
    aktuellesPixel += 1
    if aktuellesPixel == 40:
        aktuellesPixel = 0
        drawing.append([])

    if aktuellesPixel - 1 in [x + 1,x,x - 1]:
        return "#"
    return " "

for zeile in raw:

    if zeile[0] == "noop":
        takte.append(x)
        drawing[-1].append(handlePixel())

    if zeile[0] == "addx":
        takte.append(x)
        drawing[-1].append(handlePixel())
        takte.append(x)
        drawing[-1].append(handlePixel())
        x = x + int(zeile[1])   # Für nächsten Takt

summe = 0
for i in (20,60,100,140,180,220):
    summe += i*takte[i-1]

print("Ergebnis Teil 1:",summe)
print("")

for i in drawing:
    #print(len(i))
    print("".join(i))
