

with open("Tag3.txt","r") as f:
    raw = f.read().split("\n")

for n,i in enumerate(raw):

    if n % 3 != 0:
        continue

    for k in i:
        if k in raw[n + 1] and k in raw[n + 2]:
            raw[n] = k
            break


for n,i in enumerate(raw):

    if len(i) > 1:
        continue

    if i.upper() == i:  # Capital
        raw[n] = ord(i) - 38
    else:
        raw[n] = ord(i) - 96

print(sum(raw[::3]))

