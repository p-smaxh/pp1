a = 1
f = False
while f==False:
    if (a%7==0 
        and a%2==1
        and a%3==1
        and a%4==1
        and a%5==1
        and a%6==1):
        f = True
    else:
        a=a+1

print(a)