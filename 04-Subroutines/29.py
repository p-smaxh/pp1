import math

def med(tab):
    tab.sort()
    if len(tab)%2==0:
        x=int(len(tab)/2)
        return tab[x-1]
    else:
        x = math.ceil(len(tab)/2) + math.floor(len(tab)/2)
        x=int(x/2)
        return tab[x-1]
    
def dom(tab):
    tab.sort()
    tabLiczby = [0]
    tabLiczby[0]= tab[0]
    tabIlosci = [1]

    a=0
    b=0
    
    dl = len(tab)
    for x in range(0,dl-1):
        if tab[x+1]==tabLiczby[b]:
            tabIlosci[a] = tabIlosci[a]+1
        else:
            tabIlosci.append(1)
            tabLiczby.append(tab[x+1])
            b=b+1
            a=a+1


    maks = tabLiczby[tabIlosci.index(max(tabIlosci))]
    print("Dominata: ",maks)
tab2 = [2, 3, 5, 2, 9, 8, 1, 3, 9, 1, 1, 4, 7, 7, 1, 4,5]
print(len(tab2))
print(tab2)
print("Mediana: ", med(tab2))
dom(tab2)
