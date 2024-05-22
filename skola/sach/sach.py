import tkinter,random
canvas = tkinter.Canvas(width = 802,height = 802)
canvas.pack()

meno = ''
obrazky = []
sachovnica = [
    ["VezaC1", "KonC1", "StrelecC1", "KralovnaC", "KralC", "StrelecC1", "KonC1", "VezaC1"],
    ["PesiakC1", "PesiakC2", "PesiakC3", "PesiakC4", "PesiakC5", "PesiakC6", "PesiakC7", "PesiakC8"],
    ["X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X"],
    ["X", "X", "X", "X", "X", "X", "X", "X"],
    ["PesiakB1", "PesiakB2", "PesiakB3", "PesiakB4", "PesiakB5", "PesiakB6", "PesiakB7", "PesiakB8"],
    ["VezaB1", "KonB1", "StrelecB1", "KralovnaB", "KralB", "StrelecB1", "KonB1", "VezaB1"]
]
biele = True # na zmenu farby

for i in range(8):     #stlpce
    for j in range(8): #riadky
        if biele: #SWitchovanim 
            farba = 'white'
        else:
            farba = 'brown'
        canvas.create_rectangle(j*100+2,i*100+2,j*100+102,i*100+102,
                                outline = '',fill = farba, tag = "platno")
        biele = not biele
    biele = not biele

for i in range(101,113): #ulozenie do zoznamu
    meno = str(i)+'.png'
    obr = tkinter.PhotoImage(file = meno) #zoznam obrazkov
    obrazky.append(obr)
    

y = 401# stred platna od toho odratam pre prisl farbu - poloha pesiakov
x = 51 #najlavsia figurka

for i in range(8): #Pre pesiakov
    canvas.create_image(x,y-250, image = obrazky[11],tag = 'pesiakC'+str(i)) #y-250 vyska c. pesiaka
    canvas.create_image(x,y+250, image = obrazky[10],tag = 'pesiakB'+str(i)) #y+250 vyska b. pesiaka
    x += 100

x = 51
for i in range(2): #Pre veze
    canvas.create_image(x,y-350, image = obrazky[7],tag = 'vezaC'+str(i))
    canvas.create_image(x,y+350, image = obrazky[6],tag = 'vezaB'+str(i))
    x += 700

x = 151
for i in range(2): #Pre kone
    canvas.create_image(x,y-350, image = obrazky[9],tag = 'konC'+str(i))
    canvas.create_image(x,y+350, image = obrazky[8],tag = 'konB'+str(i))
    x += 500

x = 251
for i in range(2): #Pre strelcov
    canvas.create_image(x,y-350, image = obrazky[5],tag = 'strelecC'+str(i))
    canvas.create_image(x,y+350, image = obrazky[4],tag = 'strelecB'+str(i))
    x += 300

x = 351 #Kralovne
canvas.create_image(x,y-350, image = obrazky[3],tag = 'kralovnaC')
canvas.create_image(x,y+350, image = obrazky[2],tag = 'kralovnaB')

x = 451 #Krali
canvas.create_image(x,y-350, image = obrazky[1],tag = 'kralC')
canvas.create_image(x,y+350, image = obrazky[0],tag = 'kralB')

figurka = ""
x1, y1 = 0, 0
origposx = 0
origposy = 0

bpesiak = [0] * 8
cpesiak = [0] * 8

bol_vyber = False
biely = True

def check_posun(new_x, new_y):
    global sachovnica
    if origposy < new_y:
        for posun_y in range(origposy, new_y):
            print(posun_y)
            if sachovnica[posun_y][new_x] != "X":
                print("lol")
                return True
    else:
        for posun_y in range(new_y, origposy):
            print(posun_y)
            if sachovnica[posun_y][new_x] != "X":
                print("lol")
                return True
    print(sachovnica)
    print(origposx)
    print(origposy)
    print(new_x)
    print(new_y)
    sachovnica[new_y][new_x], sachovnica[origposy][origposx] = sachovnica[origposy][origposx], sachovnica[new_y][new_x]
    print(sachovnica)
    return False

def posun(event, co):
    global x1, y1, figurka, origposx, origposy, bol_vyber, biely
    x1, y1 = event.x, event.y
    if co == "vyber":
        bol_vyber = not bol_vyber
        if bol_vyber:
            figurka = canvas.gettags("current")[0]
            canvas.itemconfig("current", fill = "red")
            origposx = x1 // 100
            origposy = y1 // 100
        else:
            figurka_2 = canvas.gettags("current")[0]
            origposx_2 = x1 // 100
            origposy_2 = y1 // 100
            if figurka.startswith("pesiak"):
                if figurka[6] == "B" and ((origposx_2 == origposx + 1 and origposy_2 == origposy - 1) or (origposx_2 == origposx - 1 and origposy_2 == origposy - 1)):
                    if "C" in figurka_2 and biely:
                        x1 = x1 // 100 * 100 + 50
                        y1 = y1 // 100 * 100 + 50
                        canvas.coords(figurka, x1, y1)
                        canvas.delete(figurka_2)
                        bol_vyber = False
                if figurka[6] == "C" and ((origposx_2 == origposx + 1 and origposy_2 == origposy + 1) or (origposx_2 == origposx - 1 and origposy_2 == origposy + 1)):
                    if "B" in figurka_2 and not biely:
                        x1 = x1 // 100 * 100 + 50
                        y1 = y1 // 100 * 100 + 50
                        canvas.coords(figurka, x1, y1)
                        canvas.delete(figurka_2)
                        bol_vyber = False
            if figurka.startswith("veza"):
                if (origposx != origposx_2 and origposy == origposy_2) or (origposx == origposx_2 and origposy != origposy_2):
                    if "C" in figurka_2 and biely:
                        x1 = x1 // 100 * 100 + 50
                        y1 = y1 // 100 * 100 + 50
                        canvas.coords(figurka, x1, y1)
                        canvas.delete(figurka_2)
                        bol_vyber = False
                    if "B" in figurka_2 and not biely:
                        x1 = x1 // 100 * 100 + 50
                        y1 = y1 // 100 * 100 + 50
                        canvas.coords(figurka, x1, y1)
                        canvas.delete(figurka_2)
                        bol_vyber = False
            if figurka.startswith("strelec"):
                if (abs(origposy_2 - origposy) == abs(origposx_2 - origposx)) and origposy_2 != origposy:
                    x1 = x1 // 100 * 100 + 50
                    y1 = y1 // 100 * 100 + 50
                    canvas.coords(figurka, x1, y1)
                    canvas.delete(figurka_2)
            biely = not biely
    if co == "posun":
        polickox = x1 // 100
        polickoy = y1 // 100
        x1 = x1 // 100 * 100 + 50
        y1 = y1 // 100 * 100 + 50
        if not check_posun(polickox, polickoy):
            if figurka.startswith("pesiak"):
                    if figurka[6] == "B" and polickox == origposx and polickoy < origposy:
                        if polickoy >= origposy - 2 and bpesiak[int(figurka[7])] == 0:
                            bpesiak[int(figurka[7])] = 1
                            canvas.coords(figurka, x1, y1)
                        elif polickoy >= origposy - 1:
                            bpesiak[int(figurka[7])] = 1
                            canvas.coords(figurka, x1, y1)
                    elif figurka[6] == "C" and polickox == origposx and polickoy > origposy:
                        if polickoy <= origposy + 2 and cpesiak[int(figurka[7])] == 0:
                            cpesiak[int(figurka[7])] = 1
                            canvas.coords(figurka, x1, y1)
                        elif polickoy <= origposy + 1:
                            cpesiak[int(figurka[7])] = 1
                            canvas.coords(figurka, x1, y1)
            if figurka.startswith("veza"):
                if polickoy == origposy or polickox == origposx:
                    (polickox != origposx and polickoy == origposy) or (origposx == polickox and origposy != polickoy)
                    canvas.coords(figurka, x1, y1)
            if figurka.startswith("strelec"):
                if abs(polickoy - origposy) == abs(polickox - origposx):
                    canvas.coords(figurka, x1, y1)
            if figurka.startswith("kon"):
                if((polickoy == origposy + 2 and (polickox == origposx + 1 or polickox == origposx - 1)) or
                (polickoy == origposy - 2 and (polickox == origposx + 1 or polickox == origposx - 1)) or
                (polickox == origposx + 2 and (polickoy == origposy + 1 or polickoy == origposy - 1)) or
                (polickox == origposx - 2 and (polickoy == origposy + 1 or polickoy == origposy - 1))):
                    canvas.coords(figurka, x1, y1)
            if figurka.startswith("kralovna"):
                if((polickoy == origposy or polickox == origposx) or 
                (abs(polickoy - origposy) == abs(polickox - origposx))):
                    canvas.coords(figurka, x1, y1)
            if figurka.startswith("kral"):
                if((abs(polickoy - origposy) == 0) and (abs(polickox - origposx) == 1) or ((abs(polickoy - origposy) == 1) and (abs(polickox - origposx) == 0)) or ((abs(polickoy - origposy) == 1) and (abs(polickox - origposx) == 1))):
                    canvas.coords(figurka, x1, y1)

        figurka = ""
        biely = not biely
        bol_vyber = False


for i in range(9):
    canvas.tag_bind("pesiakB"+str(i), '<ButtonPress-1>', lambda event: posun(event,"vyber"))

for i in range(9):
    canvas.tag_bind("pesiakC"+str(i), '<ButtonPress-1>', lambda event: posun(event,"vyber"))

for i in range(2):
    canvas.tag_bind("vezaB"+str(i), '<ButtonPress-1>', lambda event: posun(event,"vyber"))

for j in range(2):
    canvas.tag_bind("vezaC"+str(i), '<ButtonPress-1>', lambda event: posun(event,"vyber"))

for i in range(2):
    canvas.tag_bind("strelecB"+str(i), '<ButtonPress-1>', lambda event: posun(event,"vyber"))

for j in range(2):
    canvas.tag_bind("strelecC"+str(i), '<ButtonPress-1>', lambda event: posun(event,"vyber"))

for i in range(2):
    canvas.tag_bind("konB"+str(i), '<ButtonPress-1>', lambda event: posun(event,"vyber"))

for j in range(2):
    canvas.tag_bind("konC"+str(i), '<ButtonPress-1>', lambda event: posun(event,"vyber"))

canvas.tag_bind("kralovnaC", '<ButtonPress-1>', lambda event: posun(event,"vyber"))
canvas.tag_bind("kralovnaB", '<ButtonPress-1>', lambda event: posun(event,"vyber"))

canvas.tag_bind("kralC", '<ButtonPress-1>', lambda event: posun(event,"vyber"))
canvas.tag_bind("kralB", '<ButtonPress-1>', lambda event: posun(event,"vyber"))

canvas.tag_bind("platno", '<ButtonPress-1>', lambda event: posun(event,"posun"))

canvas.mainloop()
