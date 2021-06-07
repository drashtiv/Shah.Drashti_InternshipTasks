class arith:
    n1=0
    n2=0

    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2

    def add(self):
        self.addition= self.n1 + self.n2
        print("The addition of two numbers is : ", self.addition)
        
    def subtract(self):
        self.subtraction=self.n1 - self.n2
        print("The subtraction of two numbers is : ", self.subtraction)

    def multiply(self) :
        self.Multiply=self.n1 * self.n2
        print("The multiplication of two numbers is : ", self.Multiply)

a=arith(5,3)
a.add()
a.subtract()
a.multiply()