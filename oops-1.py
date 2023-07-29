class ola:
    
    def __init__(self):
        self.name="aakash"
        self.age=19
    def update(self):
        self.age=20
a2=ola()
a1=ola()
a1.update()
a2.name="ansuhka"
a2.age=22
a2.update()
print(a1.name)
print(a1.age)
print(a2.name)
print(a2.age)