subor = open("textova_sprava2.txt", "r")
text = subor.read().split("\n")

for riadok in text:
    if riadok != "\n":
        slova = riadok.split(" ")
        for slovo in slova:
            slovo = slovo.replace("a", "")
            slovo = slovo.replace("e", "")
            slovo = slovo.replace("i", "")
            slovo = slovo.replace("o", "")
            slovo = slovo.replace("u", "")
            slovo = slovo.replace("y", "")            

            print(slovo.capitalize(), end="")
