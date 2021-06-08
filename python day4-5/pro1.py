class fun1:
    v1=0
    v2=0
    v3=0

    def setdata(self, v1, v2, v3):
        self.v1=v1
        self.v2=v2
        self.v3=v3

    def display(self):
        ans = self.v1 + self.v2 + self.v3
        print("The sum is :", ans)

sum=fun1()
sum.setdata(11,22,77)
sum.display()



