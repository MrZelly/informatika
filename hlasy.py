import tkinter
canvas = tkinter.Canvas(height = 500, width = 500)
canvas.pack()

awsd = open("hlasy.txt", "r")
hlasy = awsd.read().split("\n")
awsd.close()
print("Pocet hlasov:", len(hlasy))

sutaziaci = {i:0 for i in range(9000, 9011)}

for hlas in hlasy:
    sutaziaci[int(hlas)] += 1
print(sutaziaci)

for i in range(9000, 9011):
    print("Sutaziaci: {} mal {} hlasov".format(i, sutaziaci[i]))

zoradene = (sorted(sutaziaci.items(), key = lambda x:x[1]))

najvacsie = [zoradene[0]]
najmensie = [zoradene[-1]]

for i in range(1, len(sutaziaci)):
    if zoradene[i][1] == najmensie[0][1]:
        najmensie.append(zoradene[i])
    if zoradene[-i-1][1] == najvacsie[0][1]:
        najvacsie.append(zoradene[i])

for i in range(len(najvacsie)):
    print("Najviac hlasov mal sutaziaci: ", najvacsie[i])
for i in range(len(najmensie)):
    print("Najmenej hlasov mal sutaziaci: ", najmensie[i])
