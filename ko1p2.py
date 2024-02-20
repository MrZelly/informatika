zoznam = [1,2,3,10,58,16,15,9,8,55]
sortedzoznam = []

for cislo in zoznam:
    for i in range(len(zoznam) - 1):
        if len(sortedzoznam) == 0:
            sortedzoznam.append(cislo)
            break
        if i == len(sortedzoznam) - 1:
            sortedzoznam.append(cislo)
            break
        if zoznam[i] > cislo:
            sortedzoznam.insert(i, cislo)
            break

print(sortedzoznam)
