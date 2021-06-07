class fun4:
    n=0
        
    def setdata(self):
        self.n=int(input("Enter the number :"))
    
    def display(self):
        ans =self.n**2
        print("The square of the number is : " , ans)

sum=fun4()
sum.setdata()
sum.display()