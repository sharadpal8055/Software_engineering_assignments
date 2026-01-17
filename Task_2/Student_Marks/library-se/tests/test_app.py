import unittest
from src.app import MarksSystem


class TestSprint1(unittest.TestCase):

    def test_add_student_success(self):
        ms = MarksSystem()
        ms.add_student("101", "Asha")
        self.assertIn("101", ms.students)
        self.assertEqual(ms.students["101"].name, "Asha")

    def test_add_student_duplicate(self):
        ms = MarksSystem()
        ms.add_student("101", "Asha")
        with self.assertRaises(ValueError):
            ms.add_student("101", "Asha Again")

    def test_add_student_missing_fields(self):
        ms = MarksSystem()
        with self.assertRaises(ValueError):
            ms.add_student("", "Asha")
        with self.assertRaises(ValueError):
            ms.add_student("101", "")

    def test_add_marks_success(self):
        ms = MarksSystem()
        ms.add_student("101", "Asha")
        ms.add_marks("101", 88)
        self.assertEqual(ms.students["101"].marks, 88)

    def test_add_marks_out_of_range(self):
        ms = MarksSystem()
        ms.add_student("101", "Asha")
        with self.assertRaises(ValueError):
            ms.add_marks("101", 120)
        with self.assertRaises(ValueError):
            ms.add_marks("101", -5)

    def test_add_marks_unknown_student(self):
        ms = MarksSystem()
        with self.assertRaises(KeyError):
            ms.add_marks("999", 50)


class TestSprint2(unittest.TestCase):

    def test_calculate_grade_A(self):
        ms = MarksSystem()
        ms.add_student("201", "Aman")
        ms.add_marks("201", 85)
        self.assertEqual(ms.calculate_grade("201"), "A")

    def test_calculate_grade_B(self):
        ms = MarksSystem()
        ms.add_student("202", "Riya")
        ms.add_marks("202", 72)
        self.assertEqual(ms.calculate_grade("202"), "B")

    def test_calculate_grade_C(self):
        ms = MarksSystem()
        ms.add_student("203", "Neel")
        ms.add_marks("203", 45)
        self.assertEqual(ms.calculate_grade("203"), "C")

    def test_calculate_grade_no_marks(self):
        ms = MarksSystem()
        ms.add_student("204", "Isha")
        with self.assertRaises(ValueError):
            ms.calculate_grade("204")


class TestSprint3(unittest.TestCase):

    def test_generate_report_contains_header(self):
        ms = MarksSystem()
        report = ms.generate_report()
        self.assertIn("Student ID", report)
        self.assertIn("Name", report)
        self.assertIn("Marks", report)
        self.assertIn("Grade", report)

    def test_generate_report_contains_student_entry(self):
        ms = MarksSystem()
        ms.add_student("301", "Kiran")
        ms.add_marks("301", 82)
        report = ms.generate_report()
        self.assertIn("301", report)
        self.assertIn("Kiran", report)
        self.assertIn("82", report)
        self.assertIn("A", report)


if __name__ == "__main__":
    unittest.main()

