def suma(x):
    if x==1:
        return 1
    if x>1:
        return x + suma(x-1)
def sumaPrzedzial():
    suma=0
    for x in range(500):
        suma = suma+x
    return suma
print(suma(500))
print(sumaPrzedzial())