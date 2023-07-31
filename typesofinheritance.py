class A:
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working")
class B:   #single inheritance obating prop from A class
    def feature3(self):
        print("feature3 is working")
    def feature4(self):
        print("feature4 is working")
'''
class C(B):   multi-level From B it access the A class
    def feature5(self):
        print("feature5 is working")
    def feature6(self):
        print("feature6 is working")
'''

a1=A()
a1.feature1()
a1.feature2()
b1=B()
b1.feature3()
b1.feature4()

#Multiple inheritance by adding A and B in C 
class C(A,B):   #multi-level From B it access the A class
    def feature5(self):
        print("feature5 is working")
    def feature6(self):
        print("feature6 is working")
c1=C()
c1.feature3()