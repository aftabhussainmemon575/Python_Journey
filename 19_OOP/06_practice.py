class Laptop:
    Lapo_type = "SSD"

    def __init__ (self,ram,storage,color):
        self.ram = ram
        self.storage = storage
        self.color = color
    
    def lap_info (self):
        print(f"Laptop's RAM is {self.ram}, Storage is {self.storage}, color is {self.color} and laptop type is {self.Lapo_type} ")
     
lap_1 = Laptop(32,512,"Black") 
lap_2 = Laptop(16,256,"White")
lap_3 = Laptop(8,128,"Silver")       

lap_1.lap_info()
lap_2.lap_info()
lap_3.lap_info()