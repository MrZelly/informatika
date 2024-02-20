import tkinter, random
canvas = tkinter.Canvas(width = 1000, height = 700)
canvas.pack()

farby = ["red", "green", "blue", "orange", "purple", "yellow", "brown"]

def start(event):
    ciel = False
    while ciel == False:
        for i in range(7):
            canvas.move(str(i) + "r", random.randint(1, 30), 0)
            if(canvas.coords(str(i) + "r")[2] >= 900):
                ciel = True
                canvas.create_text(500, 350, text = "Vyhralo auto cislo " + str(i + 1), font="Arial 50")

            else:
                canvas.update()
        if(ciel == True):
            break
        canvas.after(50)

def auto(x, y, cislo):
    canvas.create_rectangle(x-20, y-10, x+20, y+10, fill=random.choice(farby), tag = cislo)
    canvas.create_rectangle(x-10, y-20, x+10, y-10, fill="lightblue", tag = cislo)
    canvas.create_oval(x-15, y+5, x-5, y+15, fill="grey", tag = cislo)
    canvas.create_oval(x+5, y+5, x+15, y+15, fill="grey", tag = cislo)

for i in range(7):
    auto(50, 50 + i*100, str(i) + "r")

canvas.create_rectangle(900, 0, 910, 700, fill="black")

canvas.bind_all("<space>", start)
tkinter.mainloop()
