import random

a = ""
b = ""
c = random.randint(0, 7)
d = 0
c = ""
for i in range(8):

    e = random.randint(0, 2)
    c = c + str(e)
    if e == 0:
        a = chr(random.randint(65, 90))
        b = b + a
    if e == 1:
        a = chr(random.randint(97, 122))
        b = b + a
    if e == 2:
        a = chr(random.randint(48, 57))
        b = b + a
    

print(b)
print(c)
