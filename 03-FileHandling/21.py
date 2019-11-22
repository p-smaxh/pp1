ile=0
suma=0
with open('numbersinrows.txt','r') as file:
    for line in file:
        ciag = line.split(",")
        dl = len(ciag)  
        for x in range (0,dl):
            suma = suma + int(ciag[x])
            ile=ile+1
            
print("suma liczb: ",suma)
print("ilosc liczb: ",ile)