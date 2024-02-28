import tkinter, random
sirka, vyska_canvas = 1920, 900
canvas = tkinter.Canvas(width = sirka, height = vyska_canvas, bg = "skyblue")
canvas.pack()

ide = False
obmedzene = False

farby = ["green", "red", "blue", "purple", "grey", "yellow"]

def budova(x, poschodia, farba):
    for i in range(poschodia):
        canvas.create_rectangle(x, vyska_canvas - 10 * i - 10, x - 10, vyska_canvas - 10 * i, fill = farba)

def mesto():
    for i in range(sirka//10):
        budova(sirka - i * 10, random.randint(1, vyska_canvas // 12), random.choice(farby))

mesto()

def start(event):
    global ide, obmedzene
    obmedzene = False
    ide = not ide
    old_vyska = 0
    while ide:
        if not obmedzene:
            vyska = random.randint(1, vyska_canvas // 12)
            old_vyska = vyska
        if obmedzene:
            vyska = random.randint(1, old_vyska)

        canvas.move("all", -10, 0)
        budova(sirka, vyska, random.choice(farby))
        canvas.update()
        canvas.after(25)

def obmedz(event):
    global obmedzene
    obmedzene = not obmedzene


canvas.bind_all("<Down>", obmedz)
canvas.bind_all("<space>", start)
tkinter.mainloop()


