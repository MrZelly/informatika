import tkinter, random
canvas = tkinter.Canvas(width = 880, height = 500)
canvas.pack()

x = 55
y = 250
r = 50

hra = True
cislo = random.randint(1,8)
pocetpokusov = 0
kliknutia = [0, 0, 0, 0, 0, 0, 0, 0]

canvas.create_oval(110*cislo-r-55,y-r,110*cislo+r-55,y+r,fill = 'blue', tag = "dobre")
canvas.create_oval(110*cislo-r-55,y-r,110*cislo+r-55,y+r,fill = 'red', tag = "dobree")
canvas.create_text(110*cislo-55, y, text = cislo, font = 'Arial 20', tag = "dobre")

def spravne(event):
    global hra
    canvas.delete("dobree")
    hra = False

def nespravne(event):
    global hra
    if hra:
        global kliknutia, pocetpokusov
        kliknutia[int(canvas.gettags("current")[1]) - 1] += 1
        ktory = int(canvas.gettags("current")[1])
        pocet = kliknutia[int(canvas.gettags("current")[1]) - 1]
        canvas.delete("t" + str(ktory))
        canvas.create_text(110 * ktory - 55, 330, text = pocet, tag = "t" + str(ktory))
        pocetpokusov += 1
        if pocetpokusov == 5:
            canvas.delete("all")
            hra = False
            canvas.create_text(440, 250, text = "Prehral si",font = 'Arial 20')

for i in range(1,9):
    if i != cislo:
        canvas.create_oval(x-r,y-r,x+r,y+r,fill = 'red', tag = ("zle", i))
        canvas.create_text(x,y,text = i,font = 'Arial 20', tag = ("zle", i))
    x += 110 #x = x + 110

canvas.tag_bind("zle", '<ButtonPress-1>', nespravne)
canvas.tag_bind("dobre", '<ButtonPress-1>', spravne)
canvas.tag_bind("dobree", '<ButtonPress-1>', spravne)

canvas.mainloop()