

with open("Tag3.txt","r") as f:
    raw = f.read().split("\n")

for n,i in enumerate(raw):
    raw[n] = [i[:len(i)//2] , i[len(i)//2:]]

    for k in raw[n][0]:
        if k in raw[n][1]:
            raw[n] = k
            break


for n,i in enumerate(raw):

    if i.upper() == i:  # Capital
        raw[n] = ord(i) - 38
    else:
        raw[n] = ord(i) - 96

print(sum(raw))

