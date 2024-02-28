subor = open("meteo.txt", "r")

pocet_merani = 0
merania = []
naj_teplota = ["", "", "", "-255", ""]

for riadok in subor:
    list_riadok = riadok.split()
    merania.append(list_riadok[1] + " teplota: " + list_riadok[3])
    if list_riadok[3][0] == "+":
        list_riadok[3] = list_riadok[3][1:len(list_riadok[3])-2] + "." + list_riadok[3][len(list_riadok[3])-1]
    if list_riadok[3][0] == "–":
        list_riadok[3] = "-" + list_riadok[3][1:len(list_riadok[3])-2] + "." + list_riadok[3][len(list_riadok[3])-1]
    
    if float(list_riadok[3]) > float(naj_teplota[3]):
        naj_teplota = (list_riadok)
    pocet_merani += 1

for meranie in merania:
    print(meranie)
print("Pocet merani:", pocet_merani)
print("Najvacsia teplota:", naj_teplota)

