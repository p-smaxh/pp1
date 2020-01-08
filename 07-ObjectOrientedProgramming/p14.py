import random
class Tele():
    def __init__(self,model,numer,operator):
        self.model = model
        self.numer = numer
        self.operator = operator
    def __str__(self):
        return "model telefonu: "+self.model+"\n"+"numer telefonu: "+str(self.numer)+"\n"+"operator: "+self.operator
    def dzwon(self,odbiorca):
        print("Dzwonię pod numer... "+str(odbiorca))
    def stanKonta(self):
        print(str(self.numer)+", twój stan konta wynosi "+str(random.randint(10,20))+"zł, pozdrawiamy - "+self.operator)

tel1 = Tele("samsung s8",921387210,"Play")
tel2 = Tele("jaTelefon 10",997223622,"Plus")
print(tel1)
tel1.dzwon(123987456)
tel1.stanKonta()