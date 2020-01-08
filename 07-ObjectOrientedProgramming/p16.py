class Student():
    def __init__(self,imie,nazwisko,albumNr):
        self.imie = imie
        self.nazwisko = nazwisko
        self.albumNr = albumNr
    def __str__(self):
        return f"Imie Studenta:{self.imie} \nNazwisko:{self.nazwisko} \nNumer albumu:{self.albumNr}"
    def __eq__(self,other):
        return self.albumNr==other.albumNr
    def __lt__(self,other):
        return self.albumNr < other.albumNr

s1 = Student("Anna","Tomaszewska",141820)
s2 = Student("Wojciech", "Zbych", 201003)
s3 = Student("Maja", "Kowalska", 153202)
s4 = Student("Marek", "Migiel", 138600)
lista = [s1,s2,s3,s4]
for e in lista:
    print(e)
    print()
print("-------------")
lista.sort()
for e in lista:
    print(e)
    print()