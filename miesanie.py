import tkinter, random
canvas = tkinter.Canvas(width = 880, height = 500, bg = "white")
canvas.pack()

x = 55
y = 250
r = 50

cislo = random.randint(1, 8)
canvas.create_oval()

for i in range(1,9):
    canvas.create_oval(x-r, y-r, x+r, y+r, fill = "red")
    canvas.create_text(x, y, text = i, font = "Arial 20")
    x += 110

tkinter.mainloop()