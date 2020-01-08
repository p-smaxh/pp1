class Book():
    def __init__(self,nazwa,autor,gatunek):
        self.nazwa = nazwa
        self.autor = autor
        self.gatunek = gatunek
class Papier(Book):
    def __init__(self, nazwa,autor,gatunek,liczbaStr):
            super().__init__(nazwa,autor,gatunek)
            self.liczbaStr = liczbaStr
    def __str__(self):
        return "Nazwa:\t"+self.nazwa.capitalize()+"\n"+"Autor:\t"+self.autor+"\n"+"Gatunek:\t"+self.gatunek+"\n"+"Liczba stron:\t:"+str(self.liczbaStr)
class Ebook(Book):
    def __init__(self, nazwa,autor,gatunek,plik):
            super().__init__(nazwa,autor,gatunek)
            self.plik = plik
    def __str__(self):
        return "Nazwa:\t"+self.nazwa.capitalize()+"\n"+"Autor:\t"+self.autor+"\n"+"Gatunek:\t"+self.gatunek+"\n"+"Sciezka:\t:"+self.plik+".epub"

papierowa = Papier("Mity","Jan Padawan","mitologie",150)
print(papierowa)
ebuk = Ebook("Java","Jan Programista","naukowe","JavaPodstawy")
print(ebuk)