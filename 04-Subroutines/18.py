def silnia(x):
    if x==1 or x==0:
        return 1
    if x>1:
        return x*silnia(x-1)
    
print(silnia(5))
