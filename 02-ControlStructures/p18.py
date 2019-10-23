for n in range (1,31):
    if(n%3==0):
        print("THREE")
    elif(n%5==0):
        print("FIVE")
    elif(n%5==0 and n%3==0):
        print("BINGO")
    else:
        print(n)