# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nBefore swapping:")
print(f"First number = {num1}, Second number = {num2}")

# Swapping the values in one line
num1, num2 = num2, num1

print("\nAfter swapping:")
print(f"First number = {num1}, Second number = {num2}")