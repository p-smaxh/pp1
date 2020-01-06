class University():
    # konstruktor obiektu (metoda __init__)
    def __init__(self):
    # cechy obiektu (pola)
        self.name = 'UEK'
        self.fullname= 'uniwersytet ekonomiczny w krakowie'
    # zachowania obiektu (metody)
    def print_name(self):
        print(self.name)
    def set_name(self,new_name):
        self.name = new_name
    def print_fullname(self):
        print(self.fullname)
    def set_fullname(self,new_name):
        self.fullname = new_name
    

u1 = University()
u1.print_fullname()
u1.set_fullname("AGH")
u1.print_fullname()

