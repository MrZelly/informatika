import tkinter
canvas = tkinter.Canvas(height = 500, width = 1000, bg = "white")
canvas.pack()

subor = open('nakupy.txt','r')
 
zoznam = subor.read().split("\n")
zoznam.pop()
 
 
nakupy = {i:[0,0] for i in range(6,22)}
 
for polozka in zoznam:
    hodina = int(polozka.split(":")[0])
    hodnota = int(polozka.split(" ")[-1])

    nakupy[hodina][0] += 1
    nakupy[hodina][1] += hodnota

for hodina in nakupy:
    y = 400 - nakupy[hodina][0] * 100
    y2 = 400 - nakupy[hodina][1] * 3
    x = (hodina - 6) * 30

    canvas.create_rectangle(x, y - 50, x + 30, 350, fill = "red")
    canvas.create_text(x + 15, 360, text = str(hodina))
    canvas.create_text(x + 15, 380, text = str(nakupy[hodina][0]))
    canvas.create_rectangle(x + 17 * 30, y2 - 50, x + 18 * 30, 350, fill = "blue")
    canvas.create_text(x + 15 + 17 * 30, 360, text = str(hodina))
    canvas.create_text(x + 15 + 17 + 30, 380, text = str(nakupy[hodina][0]))



canvas.mainloop()
