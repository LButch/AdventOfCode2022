

with open("Tag7.txt","r") as f:
    raw = f.read().split("\n")

tree = dict()
pfad = []

def recWrite(derPfad:list,whatToWrite,derTree:dict):
    if len(derPfad) == 1:
        derTree[derPfad[0]] = whatToWrite
        return

    if not derPfad[0] in derTree:
        derTree[derPfad[0]] = dict()

    recWrite(derPfad[1:],whatToWrite,derTree[derPfad[0]])

gesamtSumme = 0

def recGroessen(derTree):
    global gesamtSumme

    if isinstance(derTree,int):
        return derTree
    if not derTree:
        return 0

    ordnerGroesse = 0

    for ii in derTree:
        ordnerGroesse += recGroessen(derTree[ii])

    if ordnerGroesse <= 100_000:
        gesamtSumme += ordnerGroesse

    return ordnerGroesse

for zeile in raw:

    zeile = zeile.split(" ")

    if zeile[1] == "cd":
        if zeile[2] == "/":
            pfad = []
            continue

        if zeile[2] == "..":
            del pfad[-1]
            continue

        pfad.append(zeile[2])
        continue

    if zeile[1] == "ls" or zeile[0] == "dir":
        continue

    recWrite(pfad + [zeile[1]],int(zeile[0]),tree)

recGroessen(tree)

print("Ergebnis:",gesamtSumme)
