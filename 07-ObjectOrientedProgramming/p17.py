import math
class Figury():
    @staticmethod
    def poleKola(promien):
        pole = math.pi*promien**2
        return pole
    @staticmethod
    def poleProstokata(a,b):
        return a*b
    @staticmethod
    def poleTrojkata(a,h):
        return 0.5*a*h
print(round(Figury.poleKola(3),2))
print(Figury.poleProstokata(4,7))
print(Figury.poleTrojkata(6,2))