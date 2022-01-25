import tkinter, random
canvas = tkinter.Canvas(height = 600, width = 600)
canvas.pack()


def zakoduj():
    e = entry1.get()
    a = ""
    b = ""
    canvas.delete("all")
    
    for i in range(len(e)):
        a = a + str(ord(e[i]))

    a = bin(int(a))
    
    for i in range(len(a)):
        if(i == 0):
            continue
        elif(i == 1):
            continue
        else:
            b = b + a[i]

    canvas.create_text(300, 300, text = b)

def dekoduj():
    canvas.delete("all")
    e = entry1.get()
    f = int(e, 2)
    for i in range(len(str(f))):
        canvas.create_text(300 + i * 10, 300, text = str(f)[i])

entry1 = tkinter.Entry(bg = "gold", fg = "maroon", width = 10)
entry1.pack()

button1 = tkinter.Button(text = "zakoduj", bg = "skyblue", width = 10, command=zakoduj)
button1.pack()

button2 = tkinter.Button(text = "dekoduj", bg = "skyblue", width = 10, command=dekoduj)
button2.pack()
