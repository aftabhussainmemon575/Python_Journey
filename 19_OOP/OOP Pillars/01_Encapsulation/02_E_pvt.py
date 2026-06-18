class Bank_Account :
    def __init__(self,name,acc_id,balance):
        self.name = name  #public
        self.acc_id = acc_id
        self.__balance = balance #private 



acc_1 = Bank_Account("Aftab","aftahm575",100_000)
print(acc_1.__balance)  #we can't access private attributes outside the class but if we want it to give then we can give access using special functions called Getters and Seters. Let's see it's functions in next file.
