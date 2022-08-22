class Base1:
    def fn1(self):
        print("this is base class 1")
class Base2:
    def fn2(self):
        print("this is base class ")
class Child(Base1,Base2):
    def fn3(self):
        print("this is child class")

ob=Child()
ob.fn3()
ob.fn2()
ob.fn1()
