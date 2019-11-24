<<<<<<< HEAD
def rysujW(j,w):
    for x in range(0,10):
        print(j[x],"#"*w[x])
    
    
jezyk = ['Java','Python','JavaScript','C++','C#','Ruby','Perl','PHP','C','Android']
wartosci = [61,47,37,32,26,18,14,14,9,7]
rysujW(jezyk,wartosci)
=======
def fibb(x):
    if x==1 or x==2:
        return 1
    else:
        return fibb(x-1)+fibb(x-2)
    
for x in range(1,21):
    print(fibb(x))
>>>>>>> 9a3019944d9c50f898a59b6327040f23e5df8a09
