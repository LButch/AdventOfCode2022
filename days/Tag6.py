

with open("Tag6.txt","r") as f:
    raw = f.read()

# Teil 1
for i in range(4,len(raw)):
    if len(set(raw[i-4:i])) == 4:
        print("Teil 1:",i)
        break

# Teil 2
for i in range(14,len(raw)):
    if len(set(raw[i-14:i])) == 14:
        print("Teil 2:",i)
        break
