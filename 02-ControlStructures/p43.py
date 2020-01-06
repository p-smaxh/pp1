a = int(input("wprowadz liczbe"))
b = int(input("wprowadz liczbe"))
c = int(input("wprowadz liczbe"))

if (a<b<c):
    print("REZULTAT:",a,b,c)
if(a<c<b):
    print("REZULTAT:",a,c,b)
if(b<a<c):
    print("REZULTAT:",b,a,c)
if(b<c<a):
    print("REZULTAT:",b,c,a)
if(c<a<b):
    print("REZULTAT:",c,a,b)
if(c<b<a):
    print("REZULTAT:",c,b,a)