import random
def rzucKostka():
    suma=0
    print("wylosowane liczby: ",end="")
    for y in range(3):
        x = random.randint(1,6)
        print(x," ", end="")
        suma=suma+x
    print("")
    print("suma oczek: ",suma)
rzucKostka()