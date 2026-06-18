a = 5
b = 9
sum = a+b
#normal formatting    {} => place holder
print ("sum is {}".format (sum))
print ("sum of {} & {} is {}".format(a,b,sum))

#index based formatting 
print ("sum of {1} & {0} is {2}".format (a,b,sum))  #a=0 b=1 sum=2
#we can change the position of position holder using index

#value based formatting
print ("Here are the two values {a} & {b}".format(a=6,b=18))


#F-String Formatting
print (f"The sum of {a} and {b} is {a+b}")
print (f"The avg of {a} and {b} is {(a+b)/2}")   #ans = 7.0
print (f"The avg of {a} and {b} is {int((a+b)/2)} ") #ans = 7
print (f"The avg of {a} and {b} is {(a+b)//2}")  #ans = 7