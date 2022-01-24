import tkinter, random
canvas = tkinter.Canvas(height = 300, width = 300)
canvas.pack()

def zakoduj():
    e = entry1.get()
    a = ""
    b = ""
    canvas.delete("all")
    
    for i in range(len(a)):
        a = a + str(ord(e[i]))
        
    a = bin(a)
    
    print(len(a))
    
    for i in range(len(a)):
        if(i == 1):
            print(i)
        else:
            b = b + str()
            
    #b = bin(int(ord(a[])))
    #for i in range(len(a)):
    canvas.create_text(100, 100, text = b)

def dekoduj():
    canvas.delete("all")
    int(a, 2)
    print(a)
    for i in range(len(a)):
        canvas.create_text(100, 100, text = a[i],)

entry1 = tkinter.Entry(bg = "gold", fg = "maroon", width = 10)
entry1.pack()

button1 = tkinter.Button(text = "zakoduj", bg = "skyblue", width = 10, command=zakoduj)
button1.pack()

button2 = tkinter.Button(text = "dekoduj", bg = "skyblue", width = 10, command=dekoduj)
button2.pack()
