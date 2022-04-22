from CourseRequest import CourseRequest
from CourseLocation import CourseLocation
from Course import Course
from datetime import date, time
import unittest

class TestCourseRequest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setupClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        self.courserequest_1 = CourseRequest(Course("42", "System development", "Lukas"), date(2023, 3, 20), time(12),
                                             CourseLocation("405", "Universitetsparken 5"))

    def tearDown(self):
        print("tearDown\n")

    def test_set_course_date(self):
        self.courserequest_1.set_course_date(date(2023, 4, 20))
        self.assertEqual(self.courserequest_1.get_course_date(), date(2023, 4, 20))

    def test_get_course_date(self):
        self.assertEqual(self.courserequest_1.get_course_date(), date(2023, 3, 20), time(12))

    def test_set_course_time(self):
        self.courserequest_1.set_course_time(time(14))
        self.assertEqual(self.courserequest_1.get_course_time(), time(14))

    def test_get_course_time(self):
        self.assertEqual(self.courserequest_1.get_course_time(), time(12))

    def test_set_course_location(self):
        self.courserequest_1.set_course_location(CourseLocation("505", "uni4"))
        self.assertIsInstance(self.courserequest_1.get_course_location(),CourseLocation, CourseLocation("505", "uni4"))

    def test_get_course_location(self):
        self.assertIsInstance(self.courserequest_1.get_course_location(),CourseLocation, CourseLocation("405", "Universitetsparken 5"))
if __name__ == "__main__":
    unittest.main()
