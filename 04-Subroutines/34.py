def fibb(n):
    if n==1:
        return 1
    if n>1:
        return fibb(n)+fibb(n-1)
print(fibb(6))