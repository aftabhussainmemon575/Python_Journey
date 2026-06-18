class Laptops:
    laptop_type = "ssd"
    def __init__(self,ram,storage):
        self.ram = ram
        self.storage = storage

    def get_info(self): #instance method
        print(f"{self.ram} GB RAM, {self.storage} GB Storage and Laptop type is {self.laptop_type}")

l1 = Laptops(16,512)
l2 = Laptops(32,256)
l3 = Laptops(8,128)
l4 = Laptops(4,64)

l1.get_info()
        