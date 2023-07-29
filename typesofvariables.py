class car:
    wheels=4 #global variable
    
    def __init__(self):
        self.model="civic"  #instance variable
        self.color="black"
c1=car()
c2=car()

c1.model="supra"
print(c1.model,c1.wheels)
print(c1.color,c2.wheels)