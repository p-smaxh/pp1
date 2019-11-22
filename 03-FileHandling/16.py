import re
komunikat = 'wtorek - 23C, środa - 17C, czwartek 25C'
cyfry = re.findall('\d{2}',komunikat)
print(cyfry)
suma = 0
for x in range(0,3):
    suma = suma + int(cyfry[x])
    
print(suma/len(cyfry))
    
    