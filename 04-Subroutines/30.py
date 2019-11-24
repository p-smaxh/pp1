import random

def losuj():
    x = random.randint(1,50)
    return x

lp =0
ln =0
for x in range(1000):
    los = losuj()
    if los%2==0:
        lp+=1
    else:
        ln+=1

print("Dla 1000 liczb losowych z przedziału <1,50>:")
print("Liczby parzyste: ",ln/10,"%")
print("Liczby parzyste: ",lp/10,"%")