c = True 
d = False  

print (True and True) #True
print (True and False) #False   
print (False and False) #False
print (False and True) #False

print (True or True) #True
print (True or False) #True
print (False or False) #False
print (False or True) #True

print (not (True)) #False
print (not (False)) #True


#not operator reverse the value of the operand. If the operand
#  is true, it returns false. If the operand is false,
#  it returns true.

var = False 
print (not var) #True
var = True
print (not var) #False
print (not (5 > 3)) #False
print (not (5 < 3)) #True

print((5>2) and (3<4)) #True
print((5>2) and (3>4)) #False
print((5>2) or (3<4)) #True
print((5>2) or (3>4)) #True
print((5<2) or (3>4)) #False

