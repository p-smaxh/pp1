from p8 import Message
class SMS(Message):
    def __init__(self,numerNadawcy,numerOdbiorcy):
        self.numerNadawcy = numerNadawcy
        self.numerOdbiorcy = numerOdbiorcy
    def sent(self):
        print("wysyłanie sms....")
        print("od:"+"\t"+self.numerNadawcy)
        print("do:"+"\t"+self.numerOdbiorcy)
        print("tresc:"+"\t"+self.message)