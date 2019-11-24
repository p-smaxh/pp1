tab = [['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'
],['Piotr','Wyga','wygap@gop.pl']]

with open('tabdwu24.csv','w') as plik:
    plik.write('imie\t')
    plik.write('nazwisko\t')
    plik.write('email\n')
    for x in range (0,3):
        for y in range(0,3):
            plik.write(tab[x][y])
            plik.write('\t')
        plik.write("\n")
