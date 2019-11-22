import re

suma=0
plik = open('land.txt','r')
lista = re.findall('\d',plik.read())
dl = len(lista)
for x in range(0,dl):
    suma=suma+int(lista[x])
print(suma)