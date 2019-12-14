class TV():
    def __init__(self):
        self.is_on = 0
        self.channel_no = 1
        self.channels = []
    def on(self):
        self.is_on = 1
    def off(self):
        self.is_on = 0
    def set_channel(self,nr):
        self.channel_no = nr
    def show_status(self):
        if self.is_on:
            print("telewizor jest zalaczony, kanal ",self.channel_no," (",self.channels[self.channel_no-1],")")
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
lista = ["TVP1","TVP2", "Polsat", "TVN", "Filmbox"]
tv1.on()
tv1.set_channels(lista)
tv1.show_status()

tv1.show_channels()

