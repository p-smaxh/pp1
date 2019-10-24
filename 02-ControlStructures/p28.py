a= int(input("podaj a"))
b= int(input("podaj b"))

for n in range(a):
    for m in range(b):
        if (n==0 or n==a-1):
            print("*",end="")
        else:
            if(m==0 or m==b-1):
                print("*",end="")
            else:
                print(" ",end="")
    print("")