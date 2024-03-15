import tkinter,random
canvas = tkinter.Canvas(width = 800,height = 800)
canvas.pack()

meno = ''
cierne = False
obrazky = []
print(obrazky)

for i in range(8):
    for j in range(8):
        if cierne:
            canvas.create_rectangle(j*100, i*100, j*100 + 100, i*100 + 100, fill = "brown", width = 0)
        else: 
            canvas.create_rectangle(j*100, i*100, j*100 + 100, i*100 + 100, fill = "white", width = 0)
        cierne = not cierne
    cierne = not cierne

for i in range(101,113):
    meno = str(i)+'.png'
    obr = tkinter.PhotoImage(file = meno)
    
    obrazky.append(obr)
    
    x = random.randint(40,760)
    y = random.randint(40,760)

    x = random.randint(40,760)
    y = random.randint(40,760)
    
    canvas.create_image(x,y, image = obrazky[i-101])



canvas.mainloop()