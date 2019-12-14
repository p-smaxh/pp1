class Music():
    def __init__(self,author,song_name,album,year):
        self.author=author
        self.song_name=song_name
        self.album=album
        self.year=year
    def __str__(self):
        return  "wykonawca\t"+self.author + "\n"+"utwór\t"+self.song_name+"\n"+"album\t"+self.album+"\n"+"rok\t"+self.year
        
utw1=Music("Dawid Podsiadło","Nie ma fal","Małomiasteczkowy","2018")
print(utw1)