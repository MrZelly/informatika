asd = open("textova_sprava.txt", "r")
subor = asd.read()
print(subor)

dictrionary = {}

for i in range(97, 123, 1):
    dictrionary[chr(i)] = 0

pocet_pismen = 0
pocet_malych = 0
pocet_velkych = 0
pocet_cisel = 0
biele = 0

for riadok in subor:
    for pismeno in riadok:
        if pismeno in dictrionary:
            dictrionary[pismeno] += 1
        if pismeno.islower():
            pocet_malych += 1
        elif pismeno.isupper():
            pocet_velkych += 1
        elif pismeno.isnumeric():
            pocet_cisel += 1
        else:
            biele += 1
        pocet_pismen += 1

print("Pocet pismen:", pocet_pismen)
print("Pocet malych pismen:", pocet_malych)
print("Pocet pocet_velkych pismen:", pocet_velkych)
print("Pocet cisel:", pocet_cisel)
print("Pocet bielych:", biele)

subor2 = open("nepouzite_znaky", "w")

for pismeno in dictrionary:
    print(pismeno, "=", dictrionary[pismeno])
    if dictrionary[pismeno] == 0:
        subor2.write(pismeno + "\n")

asd.close()
subor2.close()
