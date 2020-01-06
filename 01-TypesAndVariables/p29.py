import random
#losowanie liczby
los1 = random.randint(1,6)

traf = int(input("zgadnij liczbę z przedziału 1-6 "))

if (los1==traf):
    print("trafiles!!!!!!!!!!")
else:
    print("pudło!!!!!!!!, odpowiedz to", los1)