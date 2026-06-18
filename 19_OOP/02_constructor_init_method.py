#__init__ method is a constructor.
#it is used to construct an object.
#we use (self) parameter whenever we wanna refer property of any object.
class student:
    def __init__ (self,name,caste,age,DOB):
        self.name = name
        self.caste =caste
        self.age = age
        self.DOB = DOB
student_1 = student("Aftab","Memon",19,2006)
student_2 = student("Altaf","Syed",20,2006)
student_3 = student("Sarang","Chandio",21,2006)
student_4 = student("Tony","Stark",53,1970)      
student_5 = student("Hisar","Syed",19,2006)
print (student_1.name,student_1.caste,student_1.age,student_1.DOB)
print (student_2.name,student_2.caste,student_2.age,student_2.DOB)
print (student_3.name,student_3.caste,student_3.age,student_3.DOB)
print (student_4.name,student_4.caste,student_4.age,student_4.DOB)
print (student_5.name,student_5.caste,student_5.age,student_5.DOB)
