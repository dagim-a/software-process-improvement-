#grade letter assigning 
GRADE_SCALE = [
    (95, "A+"),
    (85, "A"),
    (80, "A-"),
    (75, "B+"),
    (70, "B"),
    (65, "B-"),
    (60, "C+"),
    (55, "C"),
    (50, "C-"),
    (45, "D"),
]

# Values of the letter grades
GRADE_VALUES = {
    "A+": 4.0, 
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.5,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.5,
    "C": 2.0,
    "C-": 1.7,
    "D": 1.5,
    "F": 0.0
}

# student recors store in here
students = []

# a function for latter grade 
def get_letter_grade(mark):
    for minimum, letter in GRADE_SCALE:
        if mark >= minimum:
            return letter
    return "F"

# grade value function
def get_grade_value(mark):
    return GRADE_VALUES.get(get_letter_grade(mark), 0.0)

# print(get_letter_grade(100))
# print(get_letter_grade(10))
# print(get_letter_grade(50))
# print(get_letter_grade(84.9))
# print(get_letter_grade(150))
# print(get_letter_grade(10))
# print(get_letter_grade(-10))

# average mark function 
def calculate_average(marks):
    if not marks:
        return 0.0
    return sum(marks) / len(marks)

# GPA 
def calculate_gpa(courses):
    total_grade_points = 0
    total_credits = 0
    for info in courses.values():
        value = get_grade_value(info["mark"])
        credit = info["credit"]
        total_grade_points += value * credit
        total_credits += credit
    if total_credits == 0:
        return 0.0
    return total_grade_points / total_credits

# print(calculate_average([84, 98, 90]))      
# test1 = {
#     "Math": {"credit": 3, "mark": 84},
#     "Software Testing": {"credit": 4, "mark": 98},
#     "CD/CI": {"credit": 2, "mark": 90},
# }
# print(f"{calculate_gpa(test1):.2f}")        # 3.90
# test2 = {
#     "Math": {"credit": 3, "mark": 70},
#     "Physics": {"credit": 4, "mark": 55},
#     "English": {"credit": 3, "mark": 40},
# }
# print(f"{calculate_gpa(test2):.2f}")


# input for student id 
def get_student_id():
    while True:
        student_id = input("Enter student ID:  ").strip()
        if not student_id:
            print("Student ID cannot be empty.")
        elif any(s["id"].upper() == student_id.upper() for s in students):
            print("Student ID already exists.")
        else:
            return student_id

# students.append({"id": "S1"})     # fake student to test duplicates
# print("Returned:", get_student_id())   #need some fix validation


# number of course 
def get_course_count():
    while True:
        text = input("Enter number of courses: ").strip()
        if text.isdigit() and int(text) >= 1:
            return int(text)
        print("Invalid input. Please enter valid number.")

# course name input
def get_course_name(existing):
    while True:
        course = input("Enter course name: ").strip()
        if not course:
            print("course name cannot be empty.")
        elif course.lower() in (c.lower() for c in existing):
            print("Course name already exists.")
        else:
            return course

# print("Returned:", get_course_name({"Math": 80}))

# credit hour input
def get_credit_hour(course):
    while True:
        text = input(f"Enter credit hour for {course} (1-4):").strip()
        if text.isdigit() and 1 <= int(text) <= 4:
            return int(text)
        print("Invalid input. Please enter a number between 1 and 4.")

# print("Returned:", get_credit_hour("Math"))


# mark input 
def get_course_mark(course):
    while True:
        text = input(f"Enter mark for {course} (0-100):").strip()
        try:
            mark = float(text)
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 100.")
            continue
        if 0 <= mark <= 100:
            return mark
        print("Invalid input. Please enter a number between 0 and 100.")

# print("Returned:", get_course_mark("Math"))


# display a student 
def display_student(s):
    total_credits = sum(info["credit"] for info in s["courses"].values())

    print("\n" + "=" * 59)
    print(f"Student ID: {s['id']}")
    print(f"Name          : {s['name']}")
    print("\n" + "=" * 59)
    print(f"{'Course':<20}{'Credit':>7}{'Mark':>8}{'Letter Grade':<12}{'value':>7}{'Grade pt':>10}")
    for course, info in s["courses"].items():
        letter_grade = get_letter_grade(info["mark"])
        value = get_grade_value(info["mark"])
        point = value * info["credit"]
        print(f"{course:<20}{info['credit']:>7}{info['mark']:>8.2f}{letter_grade:<7}{value:>7.1f}{point:>10.2f}")
        print("-" * 59)
        print(f"Total credit hours : {total_credits}")
        print(f"Average mark       : {s['average']:.2f}")
        print(f"GPA                : {s['gpa']:.2f} / 4.00")
        print("=" * 59)


# fake = {
#     "id": "S1",
#     "name": "John Smith",
#     "courses": {
#         "Math": {"credit": 3, "mark": 84},
#         "Software Testing": {"credit": 4, "mark": 98},
#         "CD/CI": {"credit": 2, "mark": 90},
#     },
#     "average": 90.6667,
#     "gpa": 3.9,
# }
# display_student(fake)


# Add a student
def get_name():
    while True:
        name = input("Enter student name: ").strip()
        if name:
            return name
        print("Name cannot be empty.")


def add_student():
    print("\n--- Add Student ---")
    student_id = get_student_id()
    name = get_name()
    count = get_course_count()
    
    courses = {}
    for i in range(1, count + 1):
        print(f"\nCourse {i}:")
        course_name = get_course_name(courses)
        credit_hour = get_credit_hour(course_name)
        mark = get_course_mark(course_name)
        courses[course_name] = {"credit": credit_hour, "mark": mark}

    marks = [info["mark"] for info in courses.values()]
    student = {
        "id": student_id,
        "name": name,
        "courses": courses,
        "average": calculate_average(marks),
        "gpa": calculate_gpa(courses),
    }
    students.append(student)
    print("\nstudent added!")
    display_student(student)

# view all
def view_all():
    print("\n --- all students ---")
    if not students:
        print("No students found.")
        return
    print(f"{'ID':<10}{'Name':<20}{'Courses':>8}{'Average':>10}{'GPA':>7}")
    print("-" * 60)
    for s in students:
        print(f"{s['id']:<14}{s['name']:<22}{len(s['courses']):>8}{s['average']:>10.2f}{s['gpa']:>7.2f}")

# search
def search_student():
    student_id = input("Enter student ID to search: ").strip().upper()
    for s in students:
        if s["id"].upper() == student_id:
            display_student(s)
            return
    print("Student not found.")


# menu
def main():
    while True:
        print("\n==== student grade management system ====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. exit")
        choice = input("choose an option (1-4): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_all()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("invalid choice. please enter 1,2,3 or 4.")


if __name__ == "__main__":
    main()