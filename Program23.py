class Parent:
   def fn1(self):
       print("this is parent")
class Child(Parent):
   def fn2(self):
       print("this is child class")

ob=Child()
ob.fn2()
ob.fn1()
