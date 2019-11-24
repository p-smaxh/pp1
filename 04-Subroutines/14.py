def wystepuje(liczba,tablica):
    print("Liczba: ",liczba)
    print("Tablica: ", tablica)
    print("Rezultat: ",end="")
    if (liczba in tablica):
        print("Podana liczba występuje w tablicy")
    else:
        print("Podana liczba nie istnieje")
        
tab =  [15, 38, 7, 23, 14]
l = 23
wystepuje(l,tab)