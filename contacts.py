import email


contact = {
    "number": 4,
    "students":
        [
            {"name": "Sarah Holderness", "email":"sarah@example.com"},
            {"name": "Harry Potter", "email":"harry@example.com"},
            {"name": "Hermione Granger", "email":"hermione@example.com"},
            {"name": "Ron Weasley", "email":"ron@example.com"}
        ]    
}

for student in contact["students"]:
    print(student["email"])