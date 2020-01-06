from p8 import Message
class Email(Message):
    def __init__(self,adresNadawcy,adresOdbiorcy,temat):
        self.adresNadawcy = adresNadawcy
        self.adresOdbiorcy = adresOdbiorcy
        self.temat = temat
    def sent(self):
        print("wysyłanie maila....")
        print("od:"+"\t"+self.adresNadawcy)
        print("do:"+"\t"+self.adresOdbiorcy)
        print("Temat:"+"\t"+self.temat)
        print("tresc:"+"\t"+self.message)
        
