import random
suborr = open("text.txt", "r")
subor = suborr.read()
suborr.close()
subor = subor.split(" ")
#print(subor)
random.shuffle(subor)
output = ""
i = 0
for slovo in subor:
    i += 1
    output = output + " " + slovo
    if i == 5:
        output = output + "\n"
        i = 0
print(output)
