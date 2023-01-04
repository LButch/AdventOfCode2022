import numpy as np


with open("Tag8.txt","r") as f:
    raw = f.read()
    raw = np.array([np.array(list(i)) for i in raw.split("\n")])

score = np.full(raw.shape,-1)

for i in range(4):
    raw = np.rot90(raw)
    score = np.rot90(score)

    for reihe in list(range(len(raw))):
        for spalte in list(range(len(raw[0]))):
            # Jeder Punkt im Feld

            meinBaum = raw[reihe][spalte]   # Aktueller Baum
            scoreJetzt = 0
            print(meinBaum, end="\t\t")
            for baum in reversed(raw[reihe][0:spalte]):
                print(baum,end="\t")
                scoreJetzt += 1
                if baum >= meinBaum:
                    break

            print("-",scoreJetzt)
            #if not scoreJetzt:
            #    continue
            if score[reihe][spalte] > -1:
                score[reihe][spalte] *= scoreJetzt
            else:
                score[reihe][spalte] = scoreJetzt

    print("Nach",i)
    print(raw)
    print(score)
    print("")

print(np.max(score))

