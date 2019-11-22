with open('students.txt','r') as plik:
    for line in plik:
        lista = line.split(",")
        dl = len(lista)
        if (lista[2].isdigit() and int(lista[2])<30):
            print(lista[0],end="")
            print('\t',end="")
            print(lista[1],end="")
            print('\t',end="")
            print(lista[4],end="")
print()
        