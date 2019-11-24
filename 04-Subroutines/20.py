def potega(x,y):
    if y==1:
        return x
    if y>1:
        return x*potega(x,y-1)
    
print(potega(5,3))
