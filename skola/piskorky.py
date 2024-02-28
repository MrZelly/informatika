import tkinter
canvas = tkinter.Canvas(width = 500, height = 500)
canvas.pack()

mriezka = int(input("Zadaj velkost mriezky: "))

prvy = True
treba = 3

if mriezka < 3:
    mriezka = 3

grid = [mriezka*[0]for i in range(0, mriezka)]

for i in range(mriezka):
    for j in range(mriezka):
        canvas.create_rectangle(j*500/mriezka+1, i*500/mriezka+1, (j+1)*500/mriezka-1, (i+1)*500/mriezka-1, width = 2)

def klik(event):
    global prvy

    i = int(event.x/500*mriezka)
    j = int(event.y/500*mriezka)

    if grid[j][i] == 0:
        x = event.x // (500/mriezka)*500/mriezka+500/mriezka/2
        y = event.y // (500/mriezka)*500/mriezka+500/mriezka/2
        if prvy:
            canvas.create_text(x, y, text = "O", font = ("Times New Roman", int(500/mriezka/2)), fill = "Red")
            prvy = False
            grid[j][i] = 1

        
        else:                                                                 
            canvas.create_text(x, y, text = "X", font = ("Times New Roman", int(500/mriezka/2)), fill = "Blue")
            prvy = True
            grid[j][i] = 2

        

        plne = mriezka
        for k in grid:
            for l in k:
                if l == 0:
                    plne -= 1
                    break
        if plne == mriezka:
            canvas.unbind("<ButtonPress-1>")
            canvas.delete("all")
            canvas.create_text(250, 250, text = "Hra skoncila", font = "Arial 20")


canvas.bind("<ButtonPress-1>", klik)
tkinter.mainloop()