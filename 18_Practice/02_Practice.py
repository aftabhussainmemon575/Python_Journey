#Q; Find unique courses
data = [("Ayesha","Maths"),
        ("Afzal","English"),
        ("Asad","ITC"),
        ("Zafar","English")
]
unique_course = set()
for tup in data:
    unique_course.add(tup[1])

print(unique_course)