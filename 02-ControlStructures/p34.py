pesel = input("podaj pesel ")
if (int(pesel[9])%2==0):
    print("płeć: kobieta")
else:
    print("płeć: mężczyzna")
wiek = (100 - int(pesel[0:2:1]) ) + 18
print(wiek)