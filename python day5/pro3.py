import math
class cal3:
    p=0
    r=0
    t=0
    
    def __init__(self ,p ,r,t):
        self.p=p
        self.r=r
        self.t=t

    def callinterest(self):
        self.interest= self.p*(1.0 + (self.r*self.t))
        
    def display(self):
        print("the simple interest is : " , self.interest )

call=cal3(33.77,100,10)
call.callinterest()
call.display()