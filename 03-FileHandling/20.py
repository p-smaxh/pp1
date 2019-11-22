def czy_parzysta(x):
    if (x%2==0):
        return True
    else:
        return False
    
list = []
with open('numbers.txt','r') as file:
    for line in file:
        x = int(line)
        list.append(x)
dl = int(len(list))
with open('evennumbers.txt','w') as plik:
    for x in range (0,dl):
        if (czy_parzysta(list[x])==True):
            plik.write(str(list[x]))
            plik.write('\n')
