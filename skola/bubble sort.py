import random

cisla = []

for i in range(10):
    cisla.append(random.randint(0,100))

for i in range(len(cisla)):
    for j in range(len(cisla)):
        if(cisla[i] < cisla[j]):
            cisla[i], cisla[j] = cisla[j], cisla[i]