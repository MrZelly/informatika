import tkinter, random
canvas = tkinter.Canvas(width=170, height=90)
canvas.pack()


A, B, C = 0, 0, 0
GA, GB, GC = 0, 0, 0
zapnute = False
def onoff(event):
    global zapnute, A, B, C, GA, GB, GC
    zapnute = not zapnute


    for i in range(3):
        canvas.create_rectangle(10 + 50 * i, 10, 50 + 50 * i, 80)
    canvas.create_text(30, 45, text = A, font = "Arial 30", tag = "cislo1")
    canvas.create_text(80, 45, text = B, font = "Arial 30", tag = "cislo2")
    canvas.create_text(130, 45, text = C, font = "Arial 30", tag = "cislo3")
    canvas.create_text(10, 20, text="Current: ", fill = "white", font = "Arial 15", anchor="w") 

    canvas.delete("asd")

    while zapnute:
        GA, GB, GC = A, B, C
        A, B, C = random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)
        canvas.itemconfig("cislo1",text=A)
        canvas.itemconfig("cislo2",text=B)
        canvas.itemconfig("cislo3",text=C)
        canvas.update()
        canvas.after(200)
    
    if GA == GB == GC:
        canvas.delete("all")
        canvas.create_text(80, 45, text = "Vyhral si", font="Arial 20")
    else:
        canvas.delete("all")
        canvas.create_text(80, 45, text = "Prehral si", font="Arial 20", tag="asd")

def zapis(event):
    print("a")
    subor = open("historia.txt", "a")
    retazec = str(GA) + " " + str(GB) + " " + str(GC) + "\n"
    subor.write(retazec)
    subor.close()

canvas.bind_all("<Return>", zapis)
canvas.bind_all("<space>", onoff)
canvas.mainloop()
