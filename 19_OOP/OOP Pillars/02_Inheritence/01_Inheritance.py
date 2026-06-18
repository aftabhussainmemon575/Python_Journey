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
teacher_1 = Teacher("Math")
teacher_1.change_time("10 AM")
print (teacher_1.subject,teacher_1.Start_time,teacher_1.End_time)        