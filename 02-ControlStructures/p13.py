x = int(input("podaj x "))
y = int(input("podaj y "))
print(x);
print(y);
if (x>0 and y>0):
    print("punkt jest w pierwszej cwiartce")
elif (x<0 and y>0):
    print("punkt jest w drugiej cwiartce")
elif (x<0 and y<0):
    print("punkt jest w trzeciej cwiartce")
else:
    print("punkt jest w czwartej cwiartce")