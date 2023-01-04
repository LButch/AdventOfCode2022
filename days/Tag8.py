import numpy as np


with open("Tag8.txt","r") as f:
    raw = f.read()
    raw = np.array([np.array(list(i)) for i in raw.split("\n")])

sichtbar = np.zeros(raw.shape)
sichtbar[:, 0] = np.ones(len(raw))
sichtbar[:, -1] = np.ones(len(raw))
sichtbar[0] = np.ones(len(raw[0]))
sichtbar[-1] = np.ones(len(raw[0]))


for i in range(4):
    raw = np.rot90(raw)
    sichtbar = np.rot90(sichtbar)

    for reihe in list(range(len(raw)))[1:-1]:
        # Von links
        jetztMax = raw[reihe][0]
        for spalte in list(range(len(raw[0])))[1:-1]:
            if raw[reihe][spalte] > jetztMax:
                sichtbar[reihe][spalte] += 1
                jetztMax = raw[reihe][spalte]


sichtbar = np.where(sichtbar,1,0)
print(np.sum(sichtbar))

