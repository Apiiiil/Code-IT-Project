# Highest marks

marks = {
    "Shyam" : 45,
    "Hari" : 49,
    "Ram" : 78,
    "Raju" : 46
}

top_student = max(marks, key = marks.get)

print("Top Student:", top_student)
print("Highest marks:", marks[top_student])
