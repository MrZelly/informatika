import tkinter, random, threading, time
canvas = tkinter.Canvas(width = 600, height = 300, bg = "white")
canvas.pack()

farby = ["red", "blue", "green", "yellow", "purple"]
pocet_kablov = int(input("Zadajte pocet kablov: "))

spravne_cislo = random.randint(1, pocet_kablov)
cas = 60
vyhral = False
y = 145 + pocet_kablov*5

def spravne(event):
    global cas, vyhral
    cas = 0
    vyhral = True
    canvas.delete("all")
    canvas.create_text(300, 150, text = "Uspesne si zneskodnil bombu", font = "Arial 20")


def casovac():
    global cas
    while cas > 0:
        canvas.delete("cas")
        canvas.create_text(500, 150, text = cas, font = "Arial 20", tag = "cas")
        time.sleep(1)
        canvas.update()
        cas -= 1
    if not vyhral:
        canvas.delete("all")
        canvas.create_text(300, 150, text = "Vybuchol si debilko", font = "Arial 20")

    
for i in range(pocet_kablov):
    canvas.create_rectangle(50, y-i*10, 400, y+10-i*10, fill = random.choice(farby), tag = i+1)

canvas.tag_bind(int(spravne_cislo), "<ButtonPress-1>", spravne)

casovac_thread = threading.Thread(target = casovac)
casovac_thread.start()

tkinter.mainloop()