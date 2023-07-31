class A:
    def __init__(self):
        print(" a __init__")
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working")
class B(A):   #single inheritance obating prop from A class
    def __init__(self):
         print(" b __init__") #first it exc the sub class so it show class b output
    def feature3(self):
        print("feature3 is working")
    def feature4(self):
        print("feature4 is working")

a1=B()