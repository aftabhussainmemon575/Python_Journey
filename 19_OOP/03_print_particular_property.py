#To print a particular property of a particular object.
#we can use only one init method per class
class student:
    def __init__ (self,name,caste,age,DOB): #paramterized constructor, if here is only single parameter (self) the it will be called as default constructor.
        self.name = name
        self.caste =caste
        self.age = age
        self.DOB = DOB
    def student_age (self):  #now here self is basically student_1,if we are calling for student_2 then the value of self will become student_2.
        return self.age
student_1 = student("Aftab","Memon",19,2006)
student_2 = student("Tony","Stark",53,1970)      
print (student_1.student_age())
print(f"{student_1.name} is {student_1.student_age()} years old")