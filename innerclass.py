class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class laptop: #inner class
        def __init__(self):
            self.name="HP"
            self.cpu="i5"
            self.ram="8-GB"
        
        def show(self):
            print(self.name,self.cpu,self.ram)
s1=student("aakash",63)
s2=student("harsh",22)
s3=student("subbz",60)
s1.show()