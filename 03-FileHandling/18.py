list =[]
with open('numbers.txt','r') as file:
    for line in file:
        x = int(line)
        list.append(x)
list.sort()
print(list)