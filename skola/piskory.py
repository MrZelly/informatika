import tkinter
canvas = tkinter.Canvas(width = 500, height = 500)
canvas.pack()

mriezka = int(input("Zadaj velkost mriezky: "))

prvy = True

if mriezka < 3:
    mriezka = 3

for i in range(mriezka):
    for j in range(mriezka):
        canvas.create_rectangle(j*500/mriezka+1, i*500/mriezka+1, (j+1)*500/mriezka-1, (i+1)*500/mriezka-1, width = 2)

def klik(event):
    global prvy
    x = event.x // (500/mriezka)*500/mriezka+500/mriezka/2
    y = event.y // (500/mriezka)*500/mriezka+500/mriezka/2
    if prvy:
        canvas.create_text(x, y, text = "O", font = ("Times New Roman", int(500/mriezka/2)))
        prvy = False
    else:                                                                 
        canvas.create_text(x, y, text = "X", font = ("Times New Roman", int(500/mriezka/2)))
        prvy = True


canvas.bind("<ButtonPress-1>", klik)
tkinter.mainloop()
