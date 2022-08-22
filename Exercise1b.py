import math


class Rectangle:
    length = 10
    breadth = 20
    def calRectangle(self):

        print("Area of rectangle is:", Rectangle.length*Rectangle.breadth)
        print("Perimeter of a rectangle is:", 2*(Rectangle.length+Rectangle.breadth))

class Circle:
    radius=10
    def calCircle(self):
        print("Area of rectangle is:", math.pi*Circle.radius*Circle.radius)
        print("Perimeter of a circle is:",2*math.pi*Circle.radius)

class Triangle:

    def calTriangle(self,l,b,h):
        print("Perimeter of triangle: ", l + b + h)
        s=(l+b+h)/2
        print("Area of triangle: ", math.sqrt(s*(s-l)*(s-b)*(s-h)))


rect=Rectangle()
cir=Circle()
tri=Triangle()
rect.calRectangle()
cir.calCircle()
tri.calTriangle(2,3,4)
