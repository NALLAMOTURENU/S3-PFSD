class Base:
    def fn1(self):
        print("this is base class 1")
class Derived1(Base):
    def fn2(self):
        print("this is derived class 1")
class Derived2(Base):
    def fn3(self):
        print("this is derived class 2")
class Base2(Derived1,Derived2):
    def fn4(self):
        print("this is the final derived class")

ob=Base2()
ob.fn4()
ob.fn3()
ob.fn2()
ob.fn1()

