class Pojazd():
    def __init__(self,marka,rejestracja):
        self.marka = marka
        self.rejestracja = rejestracja
        self.czyWypozyczony = False
        self.przebieg = 0
    def __str__(self):
        wynik = f"Marka pojazdu:{self.marka}\nRejestracja:{self.rejestracja}\nPrzebieg:{self.przebieg}\nStatus:"
        if czyWypozyczony==True:
            wynik=wynik+"Wypożyczony"
        else:
            wynik= wynik+"Dostępny"
        return wynik
    def zmienStatus(self,czyWypozyczony):
        if czyWypozyczony:
            czyWypozyczony=False
        else:
            czyWypozyczony=True
    def zmienPrzebieg(self,przebieg,wartosc):
        self.przebieg = wartosc

class Osobowy(Pojazd):
    def __init__(self,marka,rejestracja,iloscMiejsc):
        super().__init__(marka,rejestracja)
        self.iloscMiejsc = iloscMiejsc
    def __str__(self):
        wynik = f"Marka pojazdu:{self.marka}\nRejestracja:{self.rejestracja}\nPrzebieg:{self.przebieg}\nStatus:"
        if czyWypozyczony==True:
            wynik=wynik+"Wypożyczony"
        else:
            wynik= wynik+"Dostępny"
        wynik =+ f"\nLadownosc:{self.iloscMiejsc}"
        return wynik
class Dostawczy(Pojazd):
    def __init__(self,marka,rejestracja,ladownosc):
        super().__init__(marka,rejestracja)
        self.ladownosc = ladownosc
    def __str__(self):
        wynik = f"Marka pojazdu:{self.marka}\nRejestracja:{self.rejestracja}\nPrzebieg:{self.przebieg}\nStatus:"
        if czyWypozyczony==True:
            wynik=wynik+"Wypożyczony"
        else:
            wynik= wynik+"Dostępny"
        wynik =+ f"\nLadownosc:{self.ladownosc}"
        return wynik
class Wypozyczalnia():
    def __init__(self):
        self.lista_p = []
    def dodajOsobowy(self,marka,rejestracja,iloscMiejsc):
        self.lista_p.append(Dostawczy(marka,rejestracja,iloscMiejsc))
    def dodajDostawczy(self,marka,rejestracja,ladownosc):
        self.lista_p.append(Dostawczy(marka,rejestracja,ladownosc))
    def __str__(self):
        for x in self.lista_p:
            print(f"Marka pojazdu:{self.lista_p[x].marka}\nRejestracja:{self.rejestracja}\nPrzebieg:{self.przebieg}\nStatus:")

wypozyczalnia = Wypozyczalnia()
wypozyczalnia.dodajOsobowy("Mazda","KR232323",5)
wypozyczalnia.dodajOsobowy("Volvo","WW111111",4)
wypozyczalnia.dodajOsobowy("Audi","PL555555",5)
wypozyczalnia.dodajDostawczy("Peugeot","SL979797",4000)
wypozyczalnia.dodajDostawczy("Inveco","MK5512222",5000)
wypozyczalnia.dodajDostawczy("Żuk","TK777667",3800)
print(wypozyczalnia)