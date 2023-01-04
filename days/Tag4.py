
with open("Tag4.txt","r") as f:
    raw = f.read().split("\n")

raw = [i.split(",") for i in raw]
raw = [[i.split("-"),k.split("-")] for i,k in raw]

def istEnthalten(zeile):
    elf1 = list(map(int, zeile[0]))
    elf2 = list(map(int, zeile[1]))

    if elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
        return 1
    if elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
        return 1

    return 0

ergebnis = sum(map(istEnthalten,raw))
print(ergebnis)

