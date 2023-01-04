import clipboard as clp

raw = clp.paste().replace("\r","").split("\n\n")

daten = [sum(map(int,i.split("\n"))) for i in raw]
print(daten)

daten.sort(reverse=True)
print(daten)
