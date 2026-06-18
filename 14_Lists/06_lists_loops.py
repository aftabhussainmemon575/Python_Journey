#find the index of 10 

nums = [1,2,3,10,4]       
index = 0
for val in nums:
    if val == 10:
        break
    index+=1
print ("The index value of 10 is",index)
