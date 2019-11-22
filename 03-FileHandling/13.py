list = [32, 16, 5, 8, 24, 7]
with open('tablica.txt','w') as zapis:
    for x in range (0,6):
        zapis.write(str(list[x]))
        zapis.write('\n')