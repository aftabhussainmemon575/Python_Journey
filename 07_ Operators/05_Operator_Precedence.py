#it is important to understand the order of operations in Python,
#as it can affect the outcome of your calculations. 
# The order of operations is as follows:

'''( )

**

*, 1, %

+, -

== , != , >, >=, <, <=

not

and

or '''

# Example 1
result = 2 + 3 * 4
print(result)  # Output: 14
# Example 2
result = (2 + 3) * 4
print(result)  # Output: 20
# Example 3
result = 2 ** 3 * 4
print(result)  # Output: 32
# Example 4
result = 2 + 3 * 4 ** 2
print(result)  # Output: 50
# Example 5
result = 2 + 3 * 4 ** 2 / 2
print(result)  # Output: 26.0
# Example 6
result = 2 + 3 * 4 ** 2 / 2 - 1
print(result)  # Output: 24.0
# Example 7
result = 2 + 3 * 4 ** 2 / (2 - 1)
print(result)  # Output: 50.0
# Example 8
result = 2 + 3 * 4 ** 2 / (2 - 1) > 25
print(result)  # Output: True
# Example 9
result = not (2 + 3 * 4 ** 2 / (2 - 1) > 25)
print(result)  # Output: False
# Example 10
result = (2 + 3 * 4 ** 2 / (2 - 1) > 25) and (5 > 3)
print(result)  # Output: True

