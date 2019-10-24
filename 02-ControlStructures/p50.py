list = []
liczba = int(input("podaj liczbe - "))
a=liczba
while liczba>=1:
    list.append(str(liczba%2))
    liczba=liczba//2;
list = list[::-1]
bin = ''.join(list)
print("liczba",a," w sys. binarnym - ",int(bin))