import re

tekst = 'To be, or not to be, that is the question'
count = re.findall('[aeiouy]',tekst)
print("liczba samoglosek w tekscie: ",len(count))