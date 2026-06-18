#Inheritance => Reusing attributes and methods from a Parent (Base) class.
#In this we are using the properties of a parent class to the Derived/Child class.
class Employee:
    Start_time = "8 AM"
    End_time = "7 PM"
    def change_time (self,newtime):
            self.Start_time = newtime
class Teacher (Employee):
    def __init__ (self,subject):
        self.subject = subject
class Adminstaff (Employee) :
     def __init__(self,role):
          self.role = role 
     def staff_detail(self):
          print(f"Role of the staff is {self.role} and his working time is from {self.Start_time} to {self.End_time}.")
staff1 = Adminstaff("Manager")
print (staff1.staff_detail())