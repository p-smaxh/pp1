l = 0
a = int(input("wprowadz liczbe"))
suma =a
while a!=0:

    a = int(input("wprowadz liczbe"))
    suma = suma+a
    l=l+1

print("suma liczb =",suma)
print("wprowadzono",l,"liczb")
print("srednia liczb wynosi",suma/l)