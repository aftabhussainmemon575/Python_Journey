# No compulsory parameter, No self/cls parameter, we can create it normally, it can't access class or instance attributes
#we use decorator (@staticmethod) to covert a normal function into static method.
class Laptops:
    laptop_type = "ssd"
    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage

    @classmethod   #Its a decorator,it changes the behaviour of a function, this decorator changed this function into class method.
    def class_1 (cls):    #class method
        print(f"{cls.laptop_type}")

    def get_info(self): #instance method
        print(f"{self.ram} GB RAM, {self.storage} GB Storage and Laptop type is {self.laptop_type}")

    @staticmethod     
    def discount_price (price,discount):   #static method
        final_price = price - (discount * price / 100)
        print(f"Discounted Price = {final_price}")
    
l1 = Laptops(16,512)

l1.discount_price(40_000,10)