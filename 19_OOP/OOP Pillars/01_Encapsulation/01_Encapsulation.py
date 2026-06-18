# Wrapping data & functions into single unit,this process is known as Encapsulation.     
#Data+Methods = single unit, it's basically a Class    single unit => class
#3 types of data => 1)Public 2)Protected 3)Private
class Bank_Account :
    def __init__(self,name,acc_id,balance):
        self.name = name  #public
        self.acc_id = acc_id
        self._balance = balance #(protected) by using underscore(_),  as a developer we need to understand that it's protected and we should not access it outside the class but it's possible to access it and if we use here double underscore (__) then it becomes (private) and we can't access it outside the class
    def acc_info (self):
        print (f"Acccount Holder name = {self.name}\nAccount id = {self.acc_id}\nBalance = {self._balance}")


acc_1 = Bank_Account("Aftab","aftahm575",100_000)
acc_1.acc_info()
