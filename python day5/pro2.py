import math
class fun2:
    radius=0
    def setdata(self):
        self.radius = float(input("Enter the radius of the circle :"))

    def area(self):
        self.a = math.pi*(self.radius**2)

    def display(self):
        print("The area of the circle is :" , self.a)

call=fun2()
call.setdata()
call.area()
call.display()
