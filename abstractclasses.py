from abc import ABC, abstractclassmethod
class computer:
    @abstractclassmethod
    def show(self):
        pass
class laptop(computer):
        def run(self):
            print("its running")
a=computer()
b=laptop()
a.show()
b.run()