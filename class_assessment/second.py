def display_roll_numbers_and_name(students_):
    for roll_number, name in students_.items():
        print(f"Roll Number {roll_number} -> Name {name}")


def add_new_display_modified(students_, roll_number, name):
    students_[roll_number] = name
    for roll_number, name in students_.items():
        print(f"Roll Number {roll_number} -> Name {name}")


def delete_a_student(students_, roll_number):
    if roll_number in students_:
        del students_[roll_number]


def modify_student_name(students_, roll_number, new_name):
    if roll_number in students_:
        students_[roll_number] = new_name


continue_next = True
students = {}

while (continue_next):
    roll_number = input("Enter the roll number: ")
    name = input("Enter the name: ")
    students[roll_number] = name
    choice = input("Do you wish to continue input? y/n ")
    if choice == 'n':
        continue_next = False

display_roll_numbers_and_name(students)
add_new_display_modified(students, 1, "Sogo")
delete_a_student(students, 2)
modify_student_name(students, 3, "Bankole")
