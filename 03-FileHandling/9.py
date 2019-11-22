a=1
with open('NoEducation.txt','r') as file:
    for line in file:
        print(a,line, end='')
        a=a+1