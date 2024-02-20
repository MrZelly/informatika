import random

x = 15
zoznam = []

for i in range(x):
    zoznam.append(i)

random.shuffle(zoznam)

print(zoznam)

for i in range(len(zoznam)):
    for j in range(len(zoznam)):
        if zoznam[i] < zoznam[j]:
            zoznam[j], zoznam[i] = zoznam[i], zoznam[j]

print(zoznam)
