class calculation:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2 
        
    def sum(self,a=None,b=None,c=None): #byapling we can pass no.of aruguments in the paramters
        s=0
        if a!=None and b!=None and c!=None :
            s=a+b+c 
            return s
        elif a!=None and b!=None:
            s=a+b
            return s
        else:
            s=a
            return s
    
s1=calculation(63,22)
s2=calculation(60,62)
sq=s1.sum(4,2,1)
sq1=s2.sum(2,2)
print(sq)
print(sq1)