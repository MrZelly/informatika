import tkinter
canvas = tkinter.Canvas(width = 500, height = 800)
canvas.pack()

franz_liszt = ["c", "d", "e", "f", "g", "a", "h"]

x = 10
y = -20
y_line = -120
pocet = 12

def notuj():
    global x, y, pocet, y_line
    noty = vstup.get()
    for nota in noty:
        try:
            if pocet == 12:
                y += 140
                y_line += 140
                x = 10
                pocet = 0
                for i in range(5):
                    canvas.create_line(10, y_line + 20 * i, 490, y_line + 20 * i)

            y_mod = franz_liszt.index(nota)
            canvas.create_oval(x, y - y_mod * 10 + 10, x + 30, y - y_mod * 10 - 10, width = 3)
            x += 40
            pocet += 1
        except:
            pass


vstup = tkinter.Entry()
vstup.pack()
tlacidlo = tkinter.Button(text = "Notuj", command = notuj)
tlacidlo.pack()

tkinter.mainloop()
