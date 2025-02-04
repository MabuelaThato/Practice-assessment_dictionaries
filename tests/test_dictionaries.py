
import unittest
from io import StringIO
import sys

try:
    from unittest import mock
except ImportError:
   
    import mock


from dictionaries import calculate_gpa, display_summary, create_student, add_courses, add_grades, update_grade, course_counts

# Helper function to capture print output
class captured_output:
    def __enter__(self):
        self.out = StringIO()
        self.err = StringIO()
        sys.stdout = self.out
        sys.stderr = self.err
        return self.out, self.err

    def __exit__(self, exc_type, exc_value, traceback):
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

class TestAssessment(unittest.TestCase):

    def test_calculate_gpa(self):
        grades1 = {"Math": 4.0, "Science": 3.0, "History": 2.0}
        self.assertAlmostEqual(calculate_gpa(grades1), 3.0)  # Use assertAlmostEqual for floats

        grades2 = {}
        self.assertEqual(calculate_gpa(grades2), 0.0)

        grades3 = {"Art": 4.0, "Music": 3.5}
        self.assertAlmostEqual(calculate_gpa(grades3), 3.75)

    def test_display_summary(self):
        student = {
            "name": "Alice",
            "id": 12345,
            "courses": ["Math", "Science"],
            "grades": {"Math": 3.7, "Science": 4.0}
        }
        expected_output = (
            "--- Student Summary ---\n"
            "Student Name: Alice\n"
            "Student ID: 12345\n"
            "Courses:\n"
            "Math\n"
            "Science\n"
            "Grades:\n"
            "Math: 3.7\n"
            "Science: 4.0\n"
            "GPA: 3.85\n"  # Expected GPA, adjust if your calculate_gpa has different precision
        )
        with captured_output() as (out, err):
            display_summary(student)
        output = out.getvalue()
        self.assertEqual(output, expected_output)

    def test_create_student(self):
        # Simulate user input for name and ID
        with captured_output() as (out, err), \
             mock.patch('builtins.input', side_effect=["Alice", "12345"]):
            student = create_student()

        self.assertEqual(student["name"], "Alice")
        self.assertEqual(student["id"], 12345)
        self.assertEqual(student["courses"], [])

    def test_add_courses(self):
        student = {"courses": []}
        # Simulate user input for course names
        with captured_output() as (out, err), \
             mock.patch('builtins.input', side_effect=["Math", "Science", "History"]):
            student = add_courses(student)

        self.assertEqual(student["courses"], ["Math", "Science", "History"])

    def test_add_grades(self):
        student = {"courses": ["Math", "Science", "History"]}
        # Simulate user input for grades
        with captured_output() as (out, err), \
             mock.patch('builtins.input', side_effect=["3.7", "4.0", "2.5"]):
            student = add_grades(student)

        self.assertEqual(student["grades"], {"Math": 3.7, "Science": 4.0, "History": 2.5})

    def test_update_grade(self):
        student = {
            "courses": ["Math", "Science", "History"],
            "grades": {"Math": 3.7, "Science": 4.0, "History": 2.5}
        }
        # Simulate user input for course name and new grade
        with captured_output() as (out, err), \
             mock.patch('builtins.input', side_effect=["Science", "3.5"]):
            update_grade(student)

        self.assertEqual(student["grades"]["Science"], 3.5)

    def test_course_counts(self):
        student = {"courses": ["Math", "Science", "Math", "Art", "Science", "Math"]}
        expected_counts = {"Math": 3, "Science": 2, "Art": 1}
        actual_counts = course_counts(student)

        self.assertEqual(actual_counts, expected_counts)

if __name__ == '__main__':
    unittest.main()