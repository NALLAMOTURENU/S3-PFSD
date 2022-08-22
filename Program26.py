class Base:
    def fn1(self):
        print("this is base class")
class Derived1(Base):
    def fn2(self):
        print("this is derived class 1")
class Derived2(Base):
    def fn3(self):
        print("this is derived class 2")

ob=Derived2()
ob.fn3()
ob.fn1()
ob=Derived1()
ob.fn2()
ob.fn1()
