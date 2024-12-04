import tkinter, random
canvas = tkinter.Canvas(width = 450, height = 450, bg = "lightgrey")
canvas.pack()

x = 225
y = 225

zradlo_x = 0
zradlo_y = 0

novy = False
panika = False
smery = ["Up"]

def create_zradlo():
  global zradlo_x, zradlo_y
  zradlo_x = random.randint(3, 42) * 10
  zradlo_y = random.randint(3, 42) * 10
  canvas.create_oval(zradlo_x, zradlo_y, zradlo_x + 10, zradlo_y + 10, fill = "red", tag = "zradlo")

def krok():
  global smery
  if len(smery) != 0:
    for i in range(len(smery)-1, 0, -1):
      smery[i] = smery[i-1]

create_zradlo();

def zmena(event):
  global smery
  # if novy == False:
  if (event.keysym == "Up" and smery[0] != "Down") or (event.keysym == "Down" and smery[0] != "Up") or (event.keysym == "Left" and smery[0] != "Right") or (event.keysym == "Right" and smery[0] != "Left"):
    smery[0] = event.keysym

canvas.create_oval(220, 220, 230, 230, fill = "green", tag = "a0")

canvas.bind_all("<Key>", zmena)

while True:
  if novy:
    if smery[0] == "Up":
      canvas.move("a0", 0, -10)
    elif smery[0] == "Down":
      canvas.move("a0", 0, 10)
    elif smery[0] == "Right":
      canvas.move("a0", 10, 0)
    elif smery[0] == "Left":
      canvas.move("a0", -10, 0)
    novy = False
  else:
    if smery[0] == "Up":
      canvas.move("a0", 0, -10)
    elif smery[0] == "Down":
      canvas.move("a0", 0, 10)
    elif smery[0] == "Right":
      canvas.move("a0", 10, 0)
    elif smery[0] == "Left":
      canvas.move("a0", -10, 0)
    for i in range(1, len(smery)):
      if smery[i] == "Up":
        canvas.move("a" + str(len(smery) - i), 0, -10)
      elif smery[i] == "Down":
        canvas.move("a" + str(len(smery) - i), 0, 10)
      elif smery[i] == "Right":
        canvas.move("a" + str(len(smery) - i), 10, 0)
      elif smery[i] == "Left":
        canvas.move("a" + str(len(smery) - i), -10, 0)
    krok()
  if canvas.coords("a0")[0] < 0 or canvas.coords("a0")[1] < 0:
    break
  for i in range(1, len(smery)):
    if canvas.coords("a0") == canvas.coords("a" + str(i)):
      panika = True
  if panika:
    break
  if canvas.coords("a0")[0] == zradlo_x and canvas.coords("a0")[1] == zradlo_y:
    canvas.delete("zradlo")
    novy = True
    smery.insert(1, smery[0])
    canvas.create_oval(canvas.coords("a0")[0], canvas.coords("a0")[1], canvas.coords("a0")[2], canvas.coords("a0")[3], fill = "green", tag = "a" + str(len(smery) - 1))
    create_zradlo()

  canvas.update()
  canvas.after(100)

canvas.delete("all")
canvas.create_text(225, 180, text = "Prehral si", font = "Arial 20")
canvas.create_text(225, 220, text = f"Skore si mal {len(smery) - 1}", font = "Arial 20")
canvas.mainloop()