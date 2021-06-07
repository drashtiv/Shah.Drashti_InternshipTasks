class fun5:
    l=0
    w=0

    def __init__(self,l,w):
        self.l=l
        self.w=w
    
    def calarea(self):
        self.a= self.l * self.w
    
    def display(self):
        print("The area of the Rectangle is : " , self.a)

call=fun5(3.2,3.3)
call.calarea()
call.display()