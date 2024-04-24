import tkinter
canvas = tkinter.Canvas(width=501, height=201)
canvas.pack()

obsadenost = [0] * 40

for i in range(5):
    for j in range(10):
        canvas.create_rectangle(j*50+1, (i-1)*50+1, j*50+51, (i-1)*50+51, fill = "white", tag = str(i) + str(j) + "a")
        canvas.create_text(j*50+25, (i-1)*50+25, text = str(i-1) + str(j), tag = (str(i) + str(j) + "a", "text"))

def klik_l(event):
    global obsadenost
    tag = canvas.gettags("current")[0]
    pos = int(tag[0] + tag[1]) - 10
    if obsadenost[pos] == 0:
        canvas.itemconfig(tag, fill="yellow")
        obsadenost[pos] = 1
    elif obsadenost[pos] == 1:
        canvas.itemconfig(tag, fill="red")
        obsadenost[pos] = 2
    canvas.delete("text")
    for i in range(5):
        for j in range(10):
            canvas.create_text(j*50+25, (i-1)*50+25, text = str(i-1) + str(j), tag = (str(i) + str(j) + "a", "text"))

def klik_r(event):
    global obsadenost
    tag = canvas.gettags("current")[0]
    pos = int(tag[0] + tag[1]) - 10
    if obsadenost[pos] == 2:
        canvas.itemconfig(tag, fill="yellow")
        obsadenost[pos] = 1
    elif obsadenost[pos] == 1:
        canvas.itemconfig(tag, fill="white")
        obsadenost[pos] = 0
    canvas.delete("text")
    for i in range(5):
        for j in range(10):
            canvas.create_text(j*50+25, (i-1)*50+25, text = str(i-1) + str(j), tag = (str(i) + str(j) + "a", "text"))

def uloz(event):
    temp = ""
    for i in range(4):
        for j in range(10):
            if i == 0:
                if(obsadenost[j] == 2):
                    temp = temp + str(j) + " "
                else:
                    temp = temp + "x "
            else:
                if(obsadenost[int(str(i) + str(j))] == 2):
                    temp = temp + (str(i) + str(j)) + " "
                else:
                    temp = temp + "x "
        temp = temp + "\n"
    subor = open('miestenky.txt', 'w')
    subor.write(temp)
    subor.close()
    print("zapisane")



for i in range(10, 51):
    canvas.tag_bind(str(i) + "a", '<ButtonPress-1>', klik_l)
    canvas.tag_bind(str(i) + "a", '<ButtonPress-3>', klik_r)

canvas.bind_all("<space>", uloz)

canvas.mainloop()