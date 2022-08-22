class Sum:
    def add(self,n1,n2):
        self.n1=n1
        self.n2=n2
        return n1+n2
class Addition(Sum):
    def add(self,n1,n2):
        self.n1=n1
        self.n2=n2
        return n1+n2

ob1=Addition()
print(ob1.add(2,3))
ob2=Sum()
print(ob2.add(4,5))
