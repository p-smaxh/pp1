def jestImie(imie):
    imiona = ['Janek', 'Ania', 'Wojtek' ,'Zosia']
    print("imiona: ",imiona)
    print("twoje imie: ",imie)
    if imie in imiona:
        print("wynik: twoje imie jest zawarte w tablicy")
    else:
        print("wynik: brak imienia w tablicy")
        
jestImie("Ania")