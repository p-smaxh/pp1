try:
    tab = ['niedostateczny', 'mierny', 'dostateczny', 'dobry', 'bardzo dobry', 'celujący']
    a = int(input("podaj ocene "))
    print("ocena",a,"slownie:",tab[a-1])
except ValueError:
    print("podaj prawidlowa wartosc")