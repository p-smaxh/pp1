produkt = input("podaj nazwe produktu")
with open('shoppinglist.txt','w') as file:
 file.write(produkt)