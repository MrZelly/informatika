import tkinter
canvas = tkinter.Canvas(height=500, width=500)
canvas.pack()

subor = open("zastavky.txt", "r", encoding="utf-8")
maxPocetLudi = int(subor.readline())
zastavky = []
zastavky2 = []
riadky = []

print("Maximalny pocet ludi na linke je: ", maxPocetLudi)

for line in subor:
    riadky.append(line.split())
    zastavky.append(line.split()[2:])

print("Pocet zastavok: ", len(zastavky))

for zastavka in zastavky:
    x = " ".join(zastavka)
    zastavky2.append(x)
    print(x)

pocetLudi = 0
for i in range(len(zastavky2)):
    pocetLudi -= int(riadky[i][1])
    pocetLudi += int(riadky[i][0])
    canvas.create_text(30, 50 * (i+1), text=zastavky2[i], anchor=tkinter.W)
    if(pocetLudi/maxPocetLudi < 0.33):
        canvas.create_rectangle(30, 50 * (i+1) + 10, 250 * (pocetLudi/maxPocetLudi), 50 * (i+1) + 40, fill = "green")
    elif(pocetLudi/maxPocetLudi > 0.66):
        canvas.create_rectangle(30, 50 * (i+1) + 10, 250 * (pocetLudi/maxPocetLudi), 50 * (i+1) + 40, fill = "red")
    else:
        canvas.create_rectangle(30, 50 * (i+1) + 10, 250 * (pocetLudi/maxPocetLudi), 50 * (i+1) + 40, fill = "orange")
    canvas.create_text(250 * (pocetLudi/maxPocetLudi) + 10, 50 * (i+1) + 25, text=str(pocetLudi) + " / " + str(maxPocetLudi), anchor=tkinter.W)


canvas.mainloop()