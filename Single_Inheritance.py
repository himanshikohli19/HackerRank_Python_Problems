#single Inheritance
class Person:
    def __init__(self,pid=1,name="xyz",address="pqr",gender="Female"):
        self.pid=pid
        self.name=name
        self.address=address
        self.gender=gender
        
    def input(self):
        self.pid=int(input("Enter PID:"))
        self.name=input("Enter name:")
        self.address=input("Enter address:")
        self.gender=input("Enter Gender:")
    def show(self):
        print("ID:",self.pid)
        print("Name:",self.name)
        print("address:",self.address)
        print("Gender:",self.gender)

class Emp(Person):
    def __init__(self,design="Manager",dept="",salary=134344):
        self.design=design
        self.dept=dept
        self.salary=salary
    def input(self):
        Person.input(self)
        self.design=input("Enter Designation:")
        self.dept=input("enter dept ")
        self.salary=int(input("Enter salary "))
    def show(self):
        Person.show(self)
        print("Designation ",self.design)
        print("Dept ",self.dept)
        print("Salary ",self.salary)
y=Emp()
print("Employee details ")
y.input()
y.show()
