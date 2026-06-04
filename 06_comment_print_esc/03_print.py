print ('Hello Mr Aftab')
#we can use single or double quotes to print string in python
print ('Hello " Aftab')


print('Hello', "How are you")
#we can use comma to print multiple string in one line
print('Hello' + " How are you") 
#we can also use + to print multiple string in one line but we have to add space in the end of first string or start of second string otherwise it will print both string together without space

print('Hello', 'Here is Aftab', 'i wanna ask you something.', sep = ",")
#we can use sep parameter to change the separator between 
# multiple string in one line, by default it is space but 
# we can change it to anything we want like comma, hyphen, etc.


# and (end) is used to change the end of the print statement, 
# by default it is new line but we can change it to anything we 
# want like space, comma, etc.
print('Hello', end = " ")
print('How are you?')