#Inheritance => Reusing attributes and methods from a Parent (Base) class.
#In this we are using the properties of a parent class to the Derived/Child class.
class Employee:
    Start_time = "8 AM"
    End_time = "7 PM"
class Adminstaff (Employee) :
     def __init__(self,role):
          self.role = role 
class Accountant (Adminstaff):
     def __init__(self,salary,role):
          super().__init__(role)   #called adminstaff constructor to assign 'role'.
          self.salary = salary
          self.role = role 
acc1 = Accountant(100_000,"CA")
print(acc1.role,acc1.salary,acc1.Start_time,acc1.End_time)          