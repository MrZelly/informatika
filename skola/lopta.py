import tkinter, random
canvas = tkinter.Canvas(width = 500,height=300)
canvas.pack()

Sx = 250
Sy = 20

body = 0
nechytene = 0

lopta = canvas.create_oval(Sx-10, Sy-10, Sx+10, Sy+10, fill = 'red',outline = '')
canvas.create_text(10, 10, text = f"Body: {body}", anchor=tkinter.W, font="Arial, 15", tag = "body_text")
canvas.create_text(10, 30, text = f"Nechytene: {nechytene}/10", anchor=tkinter.W, font="Arial, 15", tag = "nechytene_text")

def padanie():
    global Sx, Sy, nechytene

    if canvas.coords(lopta)[1] > 295: #updatuj Sy a Sx
        Sy,Sx = 20,random.randint(5,495)
        canvas.coords(lopta, Sx-10, Sy-10, Sx+10, Sy+10)
        nechytene += 1
        canvas.delete("nechytene_text")
        canvas.create_text(10, 30, text = f"Nechytene: {nechytene}/10", anchor=tkinter.W, font="Arial, 15", tag = "nechytene_text")
    
    if nechytene >= 10:
        canvas.delete("all")
        canvas.create_text(250, 150, text = f"Pocet uspesne chytenych lopticiek: {body}", font = "Arial 20")
    else:
        canvas.move(lopta, 0, 2)
        canvas.update()
        canvas.after(10,padanie)

def stlacene(event):
    global body, nechytene
    body += 1
    canvas.delete("body_text")
    canvas.create_text(10, 10, text = f"Body: {body}", anchor = tkinter.W, font = "Arial, 15", tag = "body_text")
    canvas.move(lopta, 0, 300-Sy)
    nechytene -= 1
    canvas.update()
    

canvas.tag_bind(lopta, "<ButtonPress-1>", stlacene)

padanie()
tkinter.mainloop()
