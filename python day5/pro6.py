class employee:

    def Name(self):
        self.name=input("Enter the name of the Employee :")
    def Designation(self):
        self.designation=input("Enter the Designation : ")

class Fieldsalary(employee):
    
    def salary(self):
        self.salary=input("Enter the Salary : ")


c=Fieldsalary()
c.Name()
c.Designation()
c.salary()