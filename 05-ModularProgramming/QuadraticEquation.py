import math
def czytajWspolczynniki():
    tab = [0,0,0]
    for x in range(0,3):
        tab[x] = input("podaj wspolczynniki rownania w kolejnosc a,b,c")
    return tab

def obliczDelte(tablica):
    delta = tablica[1]**2-4*tablica[0]*tablica[2]
    if(delta<0):
        return []
    elif(delta==0):
        x1 = -1*tablica[1]/2*tablica[0]
        return [x1]
    else:
        delta = math.sqrt(delta)
        x1 = (-1*b*delta)/2*tablica[0]
        x2 = (-1*b*delta)/2*tablica[0]
        return [x1,x2]

def wyswietlDelte(tablica):
    if len(tablica)==2:
        print("pierwiastki rownania: x1= ",tablica[0], ", x2= ",tablica[1])
    elif len(tablica)==1:
        print("pierwiastki rownania: x1= ",tablica[0])
    else:
        print("brak rozwiazan rownania")