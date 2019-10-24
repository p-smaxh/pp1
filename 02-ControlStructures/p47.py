kwota = int(input("podaj kwote w zl "))
print("kwota ", kwota," w monetach:")
reszta = kwota
print("monet 5 zl = ",kwota//5)
kwota = kwota%5
print("monet 2 zl = ",kwota//2)
kwota=kwota%2
print("monet 1 zl = ",kwota)

