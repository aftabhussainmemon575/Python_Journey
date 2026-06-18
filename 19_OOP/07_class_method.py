class Laptops:
    laptop_type = "ssd"
    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage

    @classmethod   #Its a decorator,it changes the behaviour of a function, this decorator changed this function into class method.
    def class_1 (cls):
        print(f"{cls.laptop_type}")

    def get_info(self): #instance method
        print(f"{self.ram} GB RAM, {self.storage} GB Storage and Laptop type is {self.laptop_type}")

l1 = Laptops(16,512)
l1.class_1()
#we can call class method with class as well as with object name.

        