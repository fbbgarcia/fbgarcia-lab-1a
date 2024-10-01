def load_students(filename):
    students = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if len(parts) != 8:
                print("Incorrect number of columns.")
                exit(1)
            try:
                student = {
                    'last_name': parts[0],
                    'first_name': parts[1],
                    'grade': parts[2],
                    'classroom': parts[3],
                    'bus': parts[4],
                    'gpa': parts[5],
                    'teacher_last_name': parts[6],
                    'teacher_first_name': parts[7],
                }
            except ValueError:
                print(f"Error processing line: {line}")
                exit(1)
            students.append(student)
    return students


try:
    students = load_students("students.txt")
except FileNotFoundError:
    print("students.txt is not available.")
    exit(1)


def find_students_by_lastname(students, last_name):
    found_students = [s for s in students if s['last_name'].lower() == last_name.lower()]
    for student in found_students:
        print(f"{student['last_name']},{student['first_name']},{student['grade']},{student['classroom']},{student['teacher_last_name']},{student['teacher_first_name']}")


def find_students_by_lastname_bus(students, lastname):
    found_students = [s for s in students if s['last_name'].lower() == lastname.lower()]
    for student in found_students:
        print(f"{student['last_name']},{student['first_name']},{student['bus']}")


def find_students_by_teacher_last_name(students, teacher_last_name):
    found_students = [s for s in students if s['teacher_last_name'].lower() == teacher_last_name.lower()]
    for student in found_students:
        print(f"{student['last_name']},{student['first_name']}")


def find_students_by_grade(students, grade):
    found_students = [s for s in students if s['grade'] == grade]
    for student in found_students:
        print(f"{student['last_name']},{student['first_name']}")


def find_students_by_bus(students, bus):
    found_students = [s for s in students if s['bus'] == bus]
    for student in found_students:
        print(f"{student['last_name']},{student['first_name']},{student['grade']},{student['classroom']}")


def find_students_by_grade_gpa(students, grade, find_highest=True):
    students_in_grade = [s for s in students if s['grade'] == grade]
    if len(students_in_grade) == 0:
        return None

    if find_highest:
        high_student = max(students_in_grade, key=lambda s: s['gpa'])
        print(f"{high_student['last_name']},{high_student['first_name']},{high_student['gpa']},{high_student['teacher_last_name']},{high_student['teacher_first_name']},{high_student['bus']}")
    else:
        low_student = min(students_in_grade, key=lambda s: s['gpa'])
        print(f"{low_student['last_name']},{low_student['first_name']},{low_student['gpa']},{low_student['teacher_last_name']},{low_student['teacher_first_name']},{low_student['bus']}")

def calculate_average_gpa(students, grade):
    students_in_grade = [s for s in students if s['grade'] == grade]
    if len(students_in_grade) == 0:
        return None
    try:
        average_gpa = sum(float(s['gpa']) for s in students_in_grade) / len(students_in_grade)
        print(f"{average_gpa:.2f}")
    except ValueError:
        print("Invalid GPA.")
        exit(1)


def count_students_by_grade(students):
    grade_counts = {i: 0 for i in range(7)}

    try:
        for student in students:
            grade = int(student['grade'])
            if grade in [0, 1, 2, 3, 4, 5, 6]:
                grade_counts[grade] += 1
    except ValueError:
        print("Invalid grades.")
        exit(1)

    for grade in sorted(grade_counts.keys()):
        print(f"{grade}: {grade_counts[grade]}")


while True:
    user_input = input("Enter command: ")

    if user_input.startswith('S:') or user_input.startswith('Student:'):

        if user_input.endswith(' B') or user_input.endswith(' Bus'):
            if user_input.startswith('S:'):
                lastname = user_input[2:].replace(' Bus', '').replace(' B', '').strip()
            else:
                lastname = user_input[8:].replace(' Bus', '').replace(' B', '').strip()
            find_students_by_lastname_bus(students, lastname)

        else:
            if user_input.startswith('S:'):
                lastname = user_input[2:].strip()
            else:
                lastname = user_input[8:].strip()
            find_students_by_lastname(students, lastname)

    elif user_input.startswith('T:') or user_input.startswith('Teacher:'):
        if user_input.startswith('T:'):
            teacher_last_name = user_input[2:].strip()
        else:
            teacher_last_name = user_input[8:].strip()
        find_students_by_teacher_last_name(students, teacher_last_name)

    elif user_input.startswith('G:') or user_input.startswith('Grade:'):
        if user_input.endswith("H") or user_input.endswith("High"):
            if user_input.startswith('G:'):
                grade = user_input.replace(' High', '').replace(' H', '')[2:].strip()
            else:
                grade = user_input.replace(' High', '').replace(' H', '')[6:].strip()
            find_students_by_grade_gpa(students, grade, True)

        elif user_input.endswith("L") or user_input.endswith("Low"):
            if user_input.startswith('G:'):
                grade = user_input.replace(' Low', '').replace(' L', '')[2:].strip()
            else:
                grade = user_input.replace(' Low', '').replace(' L', '')[6:].strip()
            find_students_by_grade_gpa(students, grade, False)

        else:
            if user_input.startswith('G:'):
                grade = user_input[2:].strip()
            else:
                grade = user_input[6:].strip()
            find_students_by_grade(students, grade)

    elif user_input.startswith('B:') or user_input.startswith('Bus:'):
        if user_input.startswith('B:'):
            bus = user_input[2:].strip()
        else:
            bus = user_input[4:].strip()

        find_students_by_bus(students, bus)

    elif user_input.startswith('A:') or user_input.startswith('Average:'):
        if user_input.startswith('A:'):
            grade = user_input[2:].strip()
        else:
            grade = user_input[8:].strip()
        calculate_average_gpa(students, grade)

    elif user_input in ['I', 'Info']:
        count_students_by_grade(students)

    elif user_input in ['Q', 'Quit']:
        print("Quitting the program.")
        break

    else:
        print("Unrecognized command. Please try again.")
