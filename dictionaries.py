# TODO: Step 1 - Create an empty dictionary called `student` and add the following key-value pairs:
#   - name: (string) Get the student's name from user input
#   - id: (integer) Get the student's ID number from user input
#   - courses: (list) An empty list to store the courses the student is taking
#   Print the `student` dictionary.
def create_student():
    student = {}
    student['name'] = input("Name: ").strip()
    try:
        student['student_id'] = int(input("Id: ").strip())
    except ValueError:
        print("Id must be in format: '73179398163'.")
    
    student['courses'] = []

    print(student)

# TODO: Step 2 - Ask the user to enter the names of three courses the student is taking, one at a time.
#   Add each course name to the `courses` list within the `student` dictionary.
#   Print the updated `student` dictionary.
def add_courses(student):
    for i in range(3):
       student['courses'].append()
    print(student)
       

# TODO: Step 3 - Create a new dictionary called `grades`.
#   For each course in the `student["courses"]` list, prompt the user to enter the corresponding grade for that course.
#   Store the course name as the key and the grade (as a float) as the value in the `grades` dictionary.
#   Add the `grades` dictionary to the `student` dictionary under the key "grades".
#   Print the updated `student` dictionary.
def add_grades(student):
    grades = {}
    courses = student['courses']

    for course in courses:
        try:
            grades[course] = float(input(f'{course} grade: ').strip())
        except ValueError:
            print('Invalid value for grade')
    
    student['grades'] = grades
    print(student)

# TODO: Step 4 - Write a function called `calculate_gpa(grades)` that takes the `grades` dictionary as input.
#   Assume the following grade point values:
#       A: 4.0
#       B: 3.0
#       C: 2.0
#       D: 1.0
#       F: 0.0
#   Calculate the GPA (Grade Point Average) by averaging the grade points.
#   Return the calculated GPA.
#   Handle the case where the `grades` dictionary is empty (return 0.0 in that case).
def calculate_gpa(grades):
    if len(grades) == 0:
        return 0.0

    sum = 0

    for course,grade in grades.items():
        sum += grade

    average = sum / len(grades)

    return average

# TODO: Step 5 - Write a function called `display_summary(student)` that takes the `student` dictionary as input.
#   Print the following information in a user-friendly format:
#       Student Name: (from the `student` dictionary)
#       Student ID: (from the `student` dictionary)
#       Courses: (Iterate through the `courses` list and print each course)
#       Grades: (Iterate through the `grades` dictionary and print each course and its corresponding grade)
#       GPA: (Call the `calculate_gpa()` function to get the GPA and print it)
def display_summary(student):
    print(f"Student name: {student['name']}")
    print(f"Student ID: {student['student_id']}")
    print("Courses:")
    for course in student['courses']:
        print(f"{course}")
    print('Grades:')
    for course, grade in student['grades'].items():
        print(f"{course} = {grade}")
    
    print(f"GPA: {calculate_gpa(student['grades'])}")

# TODO: Step 6 - Ask the user to enter the name of a course for which they want to update the grade.
#   Ask the user to enter the new grade.
#   Update the `grades` dictionary with the new grade.
#   Print a message confirming the grade update.
#   If the course is not found, print an appropriate message.
def update_grade(student):
    course = input("Enter the name of a course for which they want to update the grade:\n").strip()
    if course not in list(student['grades'].keys()):
        print("You do not have that course.")
    else:
        try:
            student['grades'][course] = float(input(f'Enter new grade for {course}: ').strip())
            print("Grade upgraded successfully.")
        except ValueError:
            print("Invalid input for grade.")


# TODO: Step 7 (Bonus) - Use dictionary comprehension to create a new dictionary called `course_counts`
#   where the keys are the unique course names from the `student["courses"]` list, and the values are the
#   number of times each course appears in the list.
#   Print the `course_counts` dictionary.
def course_counts(student):
    course_counts = {}
    

if __name__ == "__main__":
    student_data = create_student()
    student_data = add_courses(student_data)
    student_data = add_grades(student_data)
    display_summary(student_data)
    update_grade(student_data)
    course_counts(student_data)