<<<<<<< HEAD
import random

def losuj():
    x = random.randint(1,50)
    return x

lp =0
ln =0
for x in range(1000):
    los = losuj()
    if los%2==0:
        lp+=1
    else:
        ln+=1

print("Dla 1000 liczb losowych z przedziału <1,50>:")
print("Liczby parzyste: ",ln/10,"%")
print("Liczby parzyste: ",lp/10,"%")
=======
def suma_tablicy(tab):
    if isinstance(tab,(list)):
        if len(tab) == 0:
            return 0
        return suma_tablicy(tab[0])+suma_tablicy(tab[1:])
    else:
        return tab

 
 
 

tab = [7, 5, [3, 6, [2]], 7, [1, [2, 3, [4]], 9, 2], 4]
print(suma_tablicy(tab))
>>>>>>> 9a3019944d9c50f898a59b6327040f23e5df8a09
