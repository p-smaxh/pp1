tab =[ 15, 8, 31, 47, 2, 19]
suma =0
liczba =0 
for n in tab:
    if(n%2!=0):
        suma = suma+n
        liczba = liczba+1
        
print(suma/liczba,liczba)