class Parent:
    def fn1(self):
        print("this is parent class")
class Child1(Parent):
    def fn2(self):
        print("child1")
class Child2(Child1):
    def fn3(self):
        print("child2")

ob=Child2()
ob.fn3()
ob.fn2()
ob.fn1()
