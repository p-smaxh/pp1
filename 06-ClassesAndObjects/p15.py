class TV():
    def __init__(self):
        self.is_on = 0
        self.channel_no = 1
        self.channels = ["TVP1"]
        self.volume = 0
    def up(self):
        if self.volume<=10:
            self.volume+=1
        else:
            print("zbyt glosno!")
    def down(self):
        if self.volume>=0:
            self.volume-=1
        else:
            print("ciszej nie mozna")
    def on(self):
        self.is_on = 1
    def off(self):
        self.is_on = 0
    def set_channel(self,nr):
        self.channel_no = nr
    def show_status(self):
        if self.is_on:
            print("telewizor jest zalaczony, kanal ",self.channel_no," (",self.channels[self.channel_no-1],")")
            print("obecna glosnosc: ",self.volume)
        else:
            print("telewizor wylaczony")
    def set_channels(self, ch):
        self.channels = ch
    def show_channels(self):
        print("LISTA KANALUW TV:")
        lengh = len(self.channels)
        for x in range(0,lengh):
            print(x+1,".",self.channels[x])

tv1 = TV()
tv1.show_status()
tv1.on()
tv1.show_status()

lista = ["TVP2", "Polsat", "TVN", "Filmbox"]
tv1.set_channels(lista)
tv1.up()
tv1.up()
tv1.up()
tv1.show_status()
tv1.down()
tv1.show_status()



