class A:
    def show(self):
        print("hi aakash")
class B(A): #inheritance from a to get msg
        def show(self):
            print("hi sexy")
a1=B()
a1.show()