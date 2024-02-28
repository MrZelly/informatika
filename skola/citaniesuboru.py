import random

subor = open("slova.txt","r")
slova = []
chyby = 6
pocetchyb = 0

riadky = subor.read().split()

for i in range(0,len(riadky),2):
    slova.append(riadky[i: i + 2])

print("Pocet slov na prelozenie je:", int(len(riadky)/2))

prehodit = random.randint(0, 1)

if prehodit:
    random.shuffle(slova)
i = 0
while chyby > 0:
    print(slova[i][0])
    odpoved = input("Prelozte slovo to anglictiny: ")
    if odpoved == slova[i][1]:
        print("Spravna odpoved.")
        chyby -= 1
    else:
        pocetchyb += 1
        print("Nespravna odpoved.")
        slova.append(slova[i])
    i += 1

pocetchyb = {}
pocet2chyb = 0
slova2chyb = []
je = False

for i in range(len(slova)):
    for key in pocetchyb.keys():
        if key == slova[i][1]:
            je = True
            break
        else:
            je = False
    if je == False:
        pocetchyb[slova[i][1]] = 0
    else:
        pocetchyb[slova[i][1]] += 1

for key in pocetchyb.keys():
    if pocetchyb.get(key) >= 2:
        pocet2chyb += 1

for key in pocetchyb.keys():
    if pocetchyb.get(key) >= 2:
        slova2chyb.append(key)
print("Pocet slov s viac ako 2 chybami: " + str(pocet2chyb))
print("A boli to slova: " + str(slova2chyb))