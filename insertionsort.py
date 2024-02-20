import random

x = 15
cisla = []
sortedcisla = []

for i in range(x):
    cisla.append(i)
random.shuffle(cisla)



for cislo in cisla:
    for i in range(len(cisla)):
        if(len(sortedcisla) == 0):
            sortedcisla.insert(0, cislo)
            break
        elif(i == len(sortedcisla)):
            sortedcisla.append(cislo)
            break
        elif(cislo < sortedcisla[i]):
            sortedcisla.insert(i, cislo)
            break

print(sortedcisla)
