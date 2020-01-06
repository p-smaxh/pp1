class Student():
    university = "UEK Kraków"
    album_no = 100000
    def __init__(self,name,surrname,field):
        self.name=name
        self.surrname=surrname
        self.field=field
        self.album_no= Student.album_no
        Student.album_no+=1
    def __str__(self):
        return self.name + " " + self.surrname + "(" + str(self.album_no) + ")," + self.field+","+Student.university
s1 = Student("Wacław","POTOCKI","Informatyka stosowana")
s2 = Student("Adam","NOWICKI","Ekonomia")
s3 = Student("Rafał","Bednarz","Mikroekonomia")
print(s1)
print(s2)
print(s3)
        