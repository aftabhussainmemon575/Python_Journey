prize = int(input("Enter a number between 1 and 10: "))
match prize:
    case 1:
        print("You won an iphone")
    case 5:
        print("You won a laptop")
    case 8:
        print("You won a tablet")
    case _:        
        print("Better luck next time")    
#This is how we can use "match" "case" statement in python.
#Note: "match" "case" statement is available in python 3.10 and above.
#In "match" "case" statement, we can use "_" to match any value that is 
# not matched by the previous cases.