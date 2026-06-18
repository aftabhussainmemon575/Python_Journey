info = {
    "name" : "Aftab",
    "university" : "Szabist",
    "cgpa" : 3.80,
    "Subjects" :["ITC","English","Math"]
}
# print (info["name1"]) #wrong key
# print("Code will not execute")

#but by using .get we can run our code and it will be printed "none" if there is any wrong key

print (info.get("name1"))
print ("This code will run")