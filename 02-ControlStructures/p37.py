a = int(input("podaj 1sza liczbe"))
b = int(input("podaj 2ga liczbe"))
c = int(input("podaj 3cia liczbe"))
if(a>=b>c):
    med = b
elif(a>=c>b):
    med = c
elif(b>=a>c):
    med = a
elif(b>=c>a):
    med=c
elif(c>=a>b):
    med=a
elif(c>=b>a):
    med=b
print(med)