list =[]
with open('universities.txt','r') as file:
    for line in file:
        x = str(line)
        list.append(x)
list.sort()
print(list)
dl = int(len(list))
with open('universities.txt','w') as file:
    for x in range(0,dl):
        file.write(list[x])