values = [
    'Mitchell', '99.5', '123456'
    'Ortiz', '78.5', '813225'
    'Luu', '95.6', '823669'
    'Zimmerman', '96.8', '307760'
    'Brooks', '82.7', '827131'
    ]




search = input("What ID number do you want to find? ")

if search == values[3]:
    print(values[1])





Mitchell = {
    "name": "Mitchell",
    "average": 99.5,
    "student_id": 123456
}

Ortiz = {
    "name": "Ortiz",
    "average": 78.5,
    "student_id": 813225
}

Luu = {
    "name": "Luu",
    "average": 95.6,
    "student_id": 823669
}

Zimmerman = {
    "name": "Zimmerman",
    "average": 96.8,
    "student_id": 307760
}

Brooks = {
    "name": "Brooks",
    "average": 82.7,
    "student_id": 827131
}

while True:
    print("[1] Yes")
    print("[2] No")
    con = int(input("Do you want to search another name: "))
    if con == 1:
        print("Bye")
        break

    print()
    print("[1] Mitchell")
    print("[2] Ortiz")
    print("[3] Luu")
    print("[4] Zimmerman")
    print("[5] Brooks")
    print()

    name = int(input("Enter name: "))


    if name == 1:
        print()
        print(f"Name: {Mitchell['name']}")
        print(f"Average: {Mitchell['average']}")
        print(f"Student ID: {Mitchell['student_id']}")
        print()

    elif name == 2:
        print()
        print(f"Name: {Ortiz['name']}")
        print(f"Average: {Ortiz['average']}")
        print(f"Student ID: {Ortiz['student_id']}")
        print()

    elif name == 3:
        print()
        print(f"Name: {Luu['name']}")
        print(f"Average: {Luu['average']}")
        print(f"Student ID: {Luu['student_id']}")
        print()

    elif name == 4:
        print()
        print(f"Name: {Zimmerman['name']}")
        print(f"Average: {Zimmerman['average']}")
        print(f"Student ID: {Zimmerman['student_id']}")
        print()

    elif name == 5:
        print()
        print(f"Name: {Brooks['name']}")
        print(f"Average: {Brooks['average']}")
        print(f"Student ID: {Brooks['student_id']}")
        print()
