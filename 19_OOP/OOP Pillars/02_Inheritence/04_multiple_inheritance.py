class Teacher :
    def __init__ (self,salary):
        self.salary = salary
class Student :
    def __init__ (self,cgp):
        self.cgp = cgp
class TA(Teacher,Student):
    def __init__ (self,name,salary,cgp):
        super().__init__(salary)  #calling constructor of Teacher 
        Student.__init__(self,cgp) #calling constructor of Student by class
        self.name = name
TA_1 = TA("Aftab",50_000,3.70)        
print(TA_1.name,TA_1.salary,TA_1.cgp)