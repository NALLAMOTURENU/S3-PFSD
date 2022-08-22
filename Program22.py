class Student:
    def __init__(self,name,id,cgpa):
        self.name=name
        self.id=id
        self.cgpa=cgpa
s=Student("ABC",10,9.89)
print(getattr(s,'name'))
setattr(s,'cgpa',9.5)
print(getattr(s,'cgpa'))
delattr(s,"cgpa")
print(hasattr(s,"cgpa"))
print(hasattr(s,"id"))
