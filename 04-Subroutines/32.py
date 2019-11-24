def transpozycja(lista):
    trans = [[9,9,9], [9,9,9], [9,9,9]]

    for x in range(0,3):
        for y in range(0,3):
            trans[x][y]=lista[y][x]
    return trans

list = [[1,2,0], [0,0,3], [5,1,1]]
for x in range(0,3):
    for y in range(0,3):
        print(list[x][y]," ",end="")
    print()
print()
print(list)
print(transpozycja(list))