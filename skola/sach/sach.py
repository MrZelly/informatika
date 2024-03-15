import tkinter,random
canvas = tkinter.Canvas(width = 800,height = 800)
canvas.pack()

meno = ''
obrazky = []
print(obrazky)

for i in range(101,113):
    meno = str(i)+'.png'
    obr = tkinter.PhotoImage(file = meno)
    
    obrazky.append(obr)
    
    x = random.randint(40,760)
    y = random.randint(40,760)

    x = random.randint(40,760)
    y = random.randint(40,760)
    
    canvas.create_image(x,y, image = obrazky[i-101])

