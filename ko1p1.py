list = [1,2,3,10,58,16,15,9,8,55]

swapped = True

while swapped == True:
    swapped = False
    for i in range(len(list)):
        if(i+1 < len(list) and list[i] > list[i+1]):
            list[i], list[i+1] = list[i+1], list[i]
            swapped = True
print(list)
