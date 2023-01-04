

with open("Tag7.txt","r") as f:
    raw = f.read().split("\n")

tree = dict()
pfad = []

totalDiskSpace = 70_000_000
updateSpace = 30_000_000

def recWrite(derPfad:list,whatToWrite,derTree:dict):
    if len(derPfad) == 1:
        derTree[derPfad[0]] = whatToWrite
        return

    if not derPfad[0] in derTree:
        derTree[derPfad[0]] = dict()

    recWrite(derPfad[1:],whatToWrite,derTree[derPfad[0]])

besterOrdner = totalDiskSpace * 2
def recGroessen(derTree,benotigteGroesse = 0):

    if isinstance(derTree,int):
        return derTree
    if not derTree:
        return 0

    ordnerGroesse = 0

    for ii in derTree:
        ordnerGroesse += recGroessen(derTree[ii],benotigteGroesse)

    global besterOrdner


    if benotigteGroesse and besterOrdner - benotigteGroesse > ordnerGroesse - benotigteGroesse > 0:
        besterOrdner = ordnerGroesse

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


benotigt = (totalDiskSpace - updateSpace - recGroessen(tree)) * (-1)
print("Benötigt:",benotigt)
recGroessen(tree,benotigt)

print("Ergebnis:",besterOrdner)
