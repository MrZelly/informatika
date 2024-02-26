import tkinter
canvas = tkinter.Canvas(width = 620, height = 320, bg = "white")
canvas.pack()

subor = open("cisla.txt", "r")
cisla = list(map(int,subor.read().split("\n")))
subor.close()
print(f"Pocet cisel je: {len(cisla)}")
priemer = sum(cisla) / len(cisla)
print(f"Max je {max(cisla)}, min je {min(cisla)}, priemer je {priemer}")

parne = 0
neparne = 0
delitelne7 = []

for cislo in cisla:
    if cislo %2 == 0:
        parne += 1
    else:
        neparne += 1
    if cislo %7 == 0:
        delitelne7.append(cislo)

print(f"Parnych je {parne}, neparnych je {neparne}, delitelne 7 su {delitelne7}")

for i in range(-300, 301):
    canvas.create_rectangle(i+300, 300, i+300, 300-40*cisla.count(i)-1, outline="", fill="black")

canvas.mainloop()
