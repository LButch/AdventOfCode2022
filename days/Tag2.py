

with open("Tag2.txt","r") as f:
    spiele = f.read().replace("A","X").replace("B","Y").replace("C","Z").split("\n")

# Er, ich = Sieg
# ich, er = Niederlage
win = {
    "X" : "Y",
    "Y" : "Z",
    "Z" : "X"
}
score = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}

def einSpiel(spiel:str):
    spiel = spiel.split(" ")
    er = spiel[0]
    ich = spiel[1]

    punkte = 0
    if win[er] == ich:  # Sieg
        punkte += 6
    if er == ich:       # Unentschieden
        punkte += 3
    # Niederlage + 0

    return punkte + score[ich]


gesamtpunktzahl = sum([einSpiel(i) for i in spiele])
print(gesamtpunktzahl)
