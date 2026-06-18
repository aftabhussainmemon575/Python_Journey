#OOP=> Object Oriented Programming

# 1. What is a Class? (The Blueprint)
# A class is a user-defined data type. It acts as a logical template, blueprint, or contract that defines what data and behavior its future instances will have.
# A class does not occupy memory when it is defined.
# It bundles data (attributes) and functions (methods) into a single package


# 2. What is an Object? (The Instance)
# An object is a self-contained instance of a class. It is the physical reality created based on the class blueprint.
# An object occupies memory once it is created.
# You can create multiple independent objects from a single class, and each object can hold its own unique data.

class Student:
    Subject = "Python"
    College = "ABC"
    Year = "4th Year"

student_1 = Student()
print(student_1)
print(student_1.Subject,student_1.College,student_1.Year)

