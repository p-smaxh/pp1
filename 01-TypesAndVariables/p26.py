###wskaznik bmi
#pobieranie masy ciala
kg = int(input("podaj swoja mase w kg: "))
#pobieranie wzrostu
cm = float(input("podaj swoj wzrost w cm: "))/100
bmi = kg/(cm**2)

if (bmi<18.5):{
    print("masz niedowagę")}
elif (bmi>=18.5 and bmi <30):{
    print("masz prawidłową wagę")}
else:{
    print("masz nadwagę")}
