import random
szostka = 0
piatka = 0
czworka = 0
trojka = 0
dwojka = 0
jedynka = 0

for x in range(100):
    los = random.randrange(1,7)
    if (los==1):
        jedynka = jedynka +1
    if (los==2):
        dwojka = dwojka+1
    if (los==3):
        trojka = trojka +1
    if (los==4):
        czworka = czworka +1
    if (los==5):
        piatka = piatka +1
    if (los==6):
        szostka = szostka+1
        
print("SZÓSTKA:", szostka)
print("PIĄTKA:", piatka)
print("CZWÓRKA:", czworka)
print("TRÓJKA:", trojka)
print("DWÓJKA:", dwojka)
print("JEDYNKA:", jedynka)
