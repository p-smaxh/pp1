import math

def czy_pierwsza(n):
    a=2
    while (a<=math.sqrt(n)):
        if (n%a==0):
            return False
        a=a+1
    return True

ile = int(input("ile liczb"))
a=2
ilosc = 0;
while ilosc<ile:
    if czy_pierwsza(a)==True:
        print(a," ",end="")
        ilosc=ilosc+1
    a=a+1
