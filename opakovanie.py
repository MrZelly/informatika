import tkinter, random
canvas = tkinter.Canvas(height = 600, width = 600)
canvas.pack()




def klik():
    a = ""
    canvas.delete("all")
    text = entry1.get()
    for znak in text:
        print(ord(znak))
        a = a + str(ord(znak))
    print(a)
    for i in range(len(a)):
        canvas.create_text(100 + 10 * i,100, text = a[i], angle = random.randint(1, 360), fill = random.choice("blue", "red", "green", "yellow"))

entry1 = tkinter.Entry(bg = "gold", fg = "maroon", width = 10)
entry1.pack()

button = tkinter.Button(text = "vypis", bg = "skyblue", width = 10, command=klik)
button.pack()



