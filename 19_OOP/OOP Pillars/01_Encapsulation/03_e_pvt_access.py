#If we wanna get the access of private attributes outside the class then we need to create a function, which is a save method to get access in programming
class Bank_Account :
    def __init__(self,name,acc_id,balance):
        self.name = name  #public
        self.acc_id = acc_id #public
        self.__balance = balance #private, used double underscore to make private attribute.

    def get_balance (self):   #getter function
        return self.__balance

    def set_balance (self,newBalance):   #setter function => to add new balance
        self.__balance = newBalance
    
acc_1 = Bank_Account("Aftab","aftahm575",100_000)
acc_1.set_balance(200_000)
print (acc_1.name,acc_1.get_balance())
