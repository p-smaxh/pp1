pin = 8040

for n in range(3):
    a = int(input("podaj PIN"))
    if (a==pin):
        print("PIN poprawny")
        break
    else:
        print("pin nieprawidlowy")
    if n==2:
        print("karta zostaje zablokowana")