import tkinter
canvas = tkinter.Canvas(width = 800, height = 800)
canvas.pack()

obr = tkinter.PhotoImage(file = "~/Pictures/unico uni/lovec gyat.png")
canvas.create_image(400, 400, image = obr)

tkinter.mainloop()