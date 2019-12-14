class Ebook():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.status = 0
        self.curr_page = 1
    def show_page(self):
        print(self.curr_page)
    def open(self):
        self.status = 1
    def close(self):
        self.status = 0
    def show_status(self):
        if self.status==0:
            print("ksiazka zamknieta")
        else: print(self.title,self.author,self.pages,self.curr_page)
    def next_page(self):
        if (self.curr_page<=self.pages):
            self.curr_page+=1
        else:
            print("to juz ostatnia strona")
    def prev_page(self):
        if (curr_page>=1):
            curr_page-=1
        else:
            print("jestes na pierwszej stronie")
eb1 = Ebook("Pan Tadeusz", "Jan Brzechwa", 420)
eb1.open()
eb1.show_status()
eb1.next_page()
eb1.next_page()
eb1.next_page()
eb1.show_status()
eb1.close()
eb1.show_status()