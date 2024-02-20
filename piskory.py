import tkinter
canvas = tkinter.Canvas(width = 500, height = 500)
canvas.pack()

mriezka = int(input("Zadaj velkost mriezky: "))

if mriezka < 3:
    mriezka = 3

for i in range(mriezka):
    for j in range(mriezka):
        canvas.create_rectangle(j*500/mriezka+1, i*500/mriezka+1, (j+1)*500/mriezka-1, (i+1)*500/mriezka-1, width = 2)


tkinter.mainloop()
