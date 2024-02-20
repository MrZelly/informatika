import tkinter
canvas = tkinter.Canvas(width = 500, height = 500, bg = "white")
canvas.pack()

x = open("tajnicka.txt", "r", encoding = "utf-8")

subor = x.read().split("\n")
pozicie = subor[-1].split(" ")
subor.pop()

def stvorcek(pismeno, farba, pozicia):
    canvas.create_rectangle(pozicia[0], pozicia[1], pozicia[0] + 20, pozicia[1] + 20, fill = farba)
    canvas.create_text(pozicia[0] + 7, pozicia[1], text = pismeno, anchor = "nw", font = "Arial, 10")

for i in range(len(subor)):
    for j in range(len(subor[i])):
        x = j * 20 + 50 + (20 * (int(pozicie[0]) - int(pozicie[i])))
        y = i * 20 + 50
        if j+1 == int(pozicie[i]):
            col = "grey"
        else:
            col = "white"
        stvorcek(subor[i][j], col, [x, y])



canvas.mainloop()
