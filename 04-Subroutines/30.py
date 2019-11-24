def suma_tablicy(tab):
    if isinstance(tab,(list)):
        if len(tab) == 0:
            return 0
        return suma_tablicy(tab[0])+suma_tablicy(tab[1:])
    else:
        return tab

 
 
 

tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]
print(suma_tablicy(tab))