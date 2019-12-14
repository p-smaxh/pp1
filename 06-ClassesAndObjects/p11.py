class TV():
    def __init__(self):
        self.is_on = 0
        self.channel_no = 1
    def on(self):
        self.is_on = 1
    def off(self):
        self.is_on = 0
    def show_status(self):
        if self.is_on:
            print("telewizor jest zalaczony, kanal ",self.channel_no)
        else:
            print("telewizor wylaczony")
tv1 = TV()
tv1.show_status()
tv1.on()
tv1.show_status()
tv1.off()
tv1.show_status()


