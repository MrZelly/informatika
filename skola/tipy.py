import random
file_subor = open("tipy.txt", "r")
subor = file_subor.read().split("\n")
file_subor.close()
tipy = []
celkovy_pocet = 0
for typ in subor:
    tipyx = typ.split(" ")
    tipy.append(tipyx)

for tip in tipy:
    for cislo in tip:
        celkovy_pocet += 1

print(tipy)
print(f"Celkovy pocet tipov je: {celkovy_pocet}")

hodene = []
for i in range(5):
    hodene.append(str(random.randint(1, 50)))

print(f"Vylosovane cisla: {hodene}")

pocet_spravne = [0]*len(tipy)

for i in range(len(tipy)):
    for tipnute_cislo in tipy[i]:
        for hodene_cislo in hodene:
            if hodene_cislo == tipnute_cislo:
                pocet_spravne[i] += 1
                print(f"Spravne tipol {i+1}. tiper")

jeden = False

for i in range(len(pocet_spravne)):
    if pocet_spravne[i] >= 3:
        print(f"{i+1}. tiper mal {pocet_spravne[i]} spravne")
        jeden = True
if not jeden:
    print("Ziaden tiper nemal 3 alebo viac spravne")