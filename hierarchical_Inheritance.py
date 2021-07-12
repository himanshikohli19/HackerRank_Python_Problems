'''
Hierarchical inheritance is a kind of inheritance
where more than one class is inherited from a single parent or base class.
'''

class Person:
    def input(self):
        self.pid=int(input("Enter PID:"))
        self.name=input("Enter name:")
        self.address=input("Enter address:")
    def show(self):
        print("ID:",self.pid)
        print("Name:",self.name)
        print("address:",self.address)

class Student(Person):
    def input1(self):
        self.input()
        self.course=input("enter course ")
        self.marks=int(input("Enter marks "))
    def show1(self):
        self.show()
        print("Course ",self.course)
        print("Marks ",self.marks)
class Emp(Person):
    def input1(self):
        self.input()
        self.dept=input("enter dept ")
        self.salary=int(input("Enter salary "))
    def showValues(self):
        self.show()
        print("Dept ",self.dept)
        print("Salary ",self.salary)
x=Student()
y=Emp()
print("Student details ")
x.input1()
x.show1()
