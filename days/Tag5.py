
class stack:
    def __init__(self,startwerte:list=[]):
        self.werte = []

        for ii in startwerte:
            self.push(ii)

    def push(self,item):
        self.werte.append(item)

    def pop(self):
        return self.werte.pop(-1)

    def oben(self):
        return self.werte[-1]

    def __str__(self):
        return str(self.werte)

with open("Tag5.txt","r") as f:
    raw = f.read().split("\n\n")

boxen = raw[0].split("\n")
boxen = boxen[:-1]

seitlich = []

for i in boxen:
    seitlich.append([])

    for k in range(0,len(i),4):
        seitlich[-1].append(i[k:k + 3])

stapel = [stack() for i in range(max(map(len,seitlich)))]
#stapel = [[] for i in range(max(map(len,seitlich)))]

for i in reversed(seitlich):
    for n,k in enumerate(i):
        if k != "   ":
            stapel[n].push(k)

for i in stapel:
    print(i)

moves = raw[1].split("\n")

for move in moves:
    move = move.replace("move ","").replace("from ","").replace("to ","").split(" ")
    move = list(map(int,move))

    for i in range(move[0]):
        stapel[move[2] - 1].push(stapel[move[1] - 1].pop())

for i in stapel:
    print(i.oben())
