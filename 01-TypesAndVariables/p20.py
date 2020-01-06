'''
Obliczanie pola powierzchni i obwodu koła o zadanym promieniu
'''
import math

# ustal promień koła i PI
r=5;
pi = math.pi
# oblicz pole i obwód
pole = pi*math.pow(r,2);
obw = 2*pi*r

# wyświetl rezultaty
print("pole koła o promienu",r,"wynosi",pole)
print("obwod koła o promienu",r,"wynosi",obw)
