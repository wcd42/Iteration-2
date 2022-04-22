import unittest
from Course import Course

class TestCourse(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setupClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        self.course_1 = Course("42", "System Development", "responsible_1")

    def tearDown(self):
        print("tearDown\n")

    def test_set_course_responsible(self):
        self.course_1.set_course_responsible("responsible_2")
        self.assertEqual(self.course_1.get_course_responsible(), "responsible_2")

    def test_get_course_responsible(self):
        self.assertEqual(self.course_1.get_course_responsible(), "responsible_1")

    def test_get_course_id(self):
        self.assertEqual(self.course_1.get_course_id(), "42")

    def test_get_course_name(self):
        self.assertEqual(self.course_1.get_course_name(), "System Development")

if __name__ == "__main__":
    unittest.main()