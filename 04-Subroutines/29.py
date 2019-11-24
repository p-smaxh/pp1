def suma_cyfr(x):
    if x%10==x:
        return x
    else:
        return suma_cyfr(x//10)+x%10
    

print(suma_cyfr(889))