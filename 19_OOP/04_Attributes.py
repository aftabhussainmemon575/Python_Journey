#There are two types of attribute 
# 1) Class Attribute => Attributes which belongs to class, common for all the objects
# 2) Instance Attribute => Attributes which belongs to objects,every object can be unique
class Student :
    University = "Szabist"  #class attribute

    def __init__(self,name,age):
         self.name = name  #instance attribute
         self.age = age

stu1 = Student("Aftab",19)     #these are objects
stu2 = Student("Altaf",21)
stu3 = Student("Sarang",23)

print (stu1.name)
print (Student.University) #we can access University by both class and student name 
print (stu1.University) 
#with the object we can access both attributes but with class we can only access class attribute