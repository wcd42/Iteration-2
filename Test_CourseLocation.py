from CourseLocation import CourseLocation
import unittest

class TestCourseLocation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setupClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        self.courselocation1 = CourseLocation("205", "Universitetesparken 5")

    def tearDown(self):
        print("tearDown\n")

    def test_get_address(self):
        self.assertEqual(self.courselocation1.get_address(),"Universitetesparken 5")

    def test_set_address(self):
        self.courselocation1.set_address("Universitetsparken 4")
        self.assertEqual(self.courselocation1.get_address(), "Universitetsparken 4")


if __name__ == "__main__":
    unittest.main()