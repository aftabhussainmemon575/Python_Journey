class Product:
    count = 0
    def __init__(self,name,price):
        self.name = name 
        self.price = price
        Product.count+=1
    def get_info(self):
        print(f"The name of product is {self.name} and its price is {self.price}")
    @classmethod
    def tot_products (cls):
        print(f"Total number of total products = {cls.count} ")

    @staticmethod
    def discount_price(price,discount):
        discounted_price = price - (discount*price/100)
        print(f"Discounted price = {discounted_price}")


product_1 = Product("Phone",40_000)
product_2 = Product("Laptop", 100_000)
product_1.get_info()
Product.tot_products()
product_1.discount_price(product_1.price,10)
product_2.discount_price(product_2.price,10)    
                        