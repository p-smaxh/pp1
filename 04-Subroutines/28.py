def fibb(x):
    if x==1 or x==2:
        return 1
    else:
        return fibb(x-1)+fibb(x-2)
    
for x in range(1,21):
    print(fibb(x))