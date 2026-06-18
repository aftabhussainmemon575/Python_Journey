color = (input("Enter traffic lights color: "))
match color: 
    case "red":
     print ("STOP")
    case "yellow":
     print("LOOK")
    case "green":
     print("GO")
    case _:
     print ("Wrong color")