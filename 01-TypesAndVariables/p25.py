numer = input("podaj numer rachunku ");
a=0


while a<26:
    print(numer[a], end="")
    if ((a+1)%4==0):{
        print(" ", end="")}
    a = a+1