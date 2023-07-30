class student:
  
    school="rks"
    
    def __init__(self,m1,m2,m3): #instant method
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    @classmethod    #class method
    def info(cls):
        return cls.school      
    
    @staticmethod   #static method
    def sec():
        print("this is A section")
    
    def avg(self):
        return(self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1

    def set_m1(self):
        return self.m1

s1=student(54,95,95)
s2=student(23,98,91)
print(s1.avg())
print(s2.avg())
print(s1.set_m1())
print(s1.get_m1())
print(student.info())
print(student.sec())