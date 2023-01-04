

with open("Tag2.txt","r") as f:
    spiele = f.read().replace("A","X").replace("B","Y").replace("C","Z").split("\n")

# Er, ich = Sieg
# ich, er = Niederlage
win = {
    "X" : "Y",  # Verlieren
    "Y" : "Z",  # Unentschieden
    "Z" : "X"   # Gewinnen
}
score = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}
lose = dict(zip(win.values(), win.keys())) # Gegenteil von win

def einSpiel(spiel:str):
    spiel = spiel.split(" ")
    er = spiel[0]
    ich = spiel[1]

    if ich == "Z":  # Gewinnen
        ich = win[er]
    elif ich == "Y":    # Unentschieden
        ich = er
    else:   # Verlieren
        ich = lose[er]

    punkte = 0
    if win[er] == ich:  # Sieg
        punkte += 6
    if er == ich:       # Unentschieden
        punkte += 3
    # Niederlage + 0

    return punkte + score[ich]


gesamtpunktzahl = sum([einSpiel(i) for i in spiele])
print(gesamtpunktzahl)
