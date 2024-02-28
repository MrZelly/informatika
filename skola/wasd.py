import tkinter, random
canvas = tkinter.Canvas(width = 500, height = 500)
canvas.pack()

hrac = canvas.create_oval(240,240,250,250, fill = "blue", tag = "hrac", outline = "")
pocet = 5
body = 0

canvas.create_text(30, 20, text = "Body: " + str(body), font = "Arial 10", tag = "body")

def potrava(i):
    y = random.randint(0, 40) * 10
    x = random.randint(0, 40) * 10

    canvas.create_oval(x, y, x + 10, y + 10, fill = "red", tag = "potrava" + str(i), outline = "")

for i in range(pocet):
    potrava(i)

def koniec():
    global body
    print("Tvoje score je:", body)
    canvas.destroy()
    exit()

def move(event):
    global body

    if event.keysym == "w":
        if canvas.coords(hrac)[1] != 0:
            canvas.move(hrac, 0, -10)
    if event.keysym == "a":
        if canvas.coords(hrac)[0] != 0:
            canvas.move(hrac, -10, 0)
    if event.keysym == "s":
        if canvas.coords(hrac)[3] != 500:
            canvas.move(hrac, 0, 10)
    if event.keysym == "d":
        if canvas.coords(hrac)[2] != 500:
            canvas.move(hrac, 10, 0)
    
    for i in range(pocet):
        if canvas.coords("potrava" + str(i)) == canvas.coords(hrac):
            body += 1
            canvas.delete("body")
            canvas.delete("potrava" + str(i))
            potrava(i)
            canvas.create_text(30, 20, text = "Body: " + str(body), font = "Arial 10", tag = "body")
    canvas.update()  

canvas.bind_all("<Key>", move)
canvas.after(10000, koniec)
canvas.mainloop()
