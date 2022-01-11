vstup = input("zadaj text: ")
posun = input("zadaj pocet posunu: ")
out = ""
a = 0

for char in vstup:
    a = ord(char)
    for i in range(int(posun)):
        if a == 90 or a == 122:
            a = a - 26 
        a = a + 1
    out = out + chr(a)

print(out)


vstup2 = input("zadaj text na odsifrovanie: ")
posun2 = input("zadaj pocet posunu: ")
out2 = ""
b = 0

for char2 in vstup2:
    b = ord(char2)
    for i in range(int(posun2)):
        if b == 65 or b == 97:
            b = b + 26            
        b = b - 1
    out2 = out2 + chr(b)

print(out2)
