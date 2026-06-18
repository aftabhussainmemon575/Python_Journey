#For To find who teaches English
data = [("Ayesha","Maths"),
        ("Afzal","English"),
        ("Asad","ITC"),
        ("Zafar","English")
]
for name,course in data:
    if (course=="English"):
        print(name)