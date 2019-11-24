def podatek(d):
    if d>5000:
        return 5000*0.17 + (d-5000)*0.32
    else:
        return d*0.17
    
x = int(input("podaj dochod: "))
print("podatek nalezny: ",podatek(x))