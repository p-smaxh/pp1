a = int(input("podaj a: "))
b = int(input("podaj b: "))
c = int(input("podaj c: "))
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + d ** (1/2)) / 2 * a
    x2 = (-b - d ** (1/2)) / 2 * a
    print(x1,x2)
elif d == 0:
    x0 = -b / (2 * a)
    print(x0)
else:
    print('brak rozwiązań')