a = int(input("Podaj limit prędkości (km/h)"))
b = int(input("Podaj prędkość pojazdu (km/h)"))

if(b-a<=0):
    print("nie przekroczono prędkosci")
elif(b-a<=10):
    print("Mandat:",5*(b-a))
else:
    print("Mandat:",15*(b-a)-100)