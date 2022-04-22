import unittest
from Employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setupClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")


    def setUp(self):
        self.employee_1 = Employee("William", "Devlin", "2103981527", "23957361", "w.charels.devlin@gmail.com")

    def tearDown(self):
        print("tearDown\n")

    def test_get_first_name(self):
        self.assertEqual(self.employee_1.get_first_name(), "William")

    def test_set_first_name(self):

        self.employee_1.set_first_name("Lukas")
        self.assertEqual(self.employee_1.get_first_name(), "Lukas")

    def test_get_last_name(self):
        self.assertEqual(self.employee_1.get_last_name(), "Devlin")

    def test_set_last_name(self):

        self.employee_1.set_last_name("Sieben")
        self.assertEqual(self.employee_1.get_last_name(), "Sieben")

    def test_get_cpr_number(self):
        self.assertEqual(self.employee_1.get_cpr_number(), "2103981527")

    def test_set_cpr_number(self):

        self.employee_1.set_cpr_number("2103981529")
        self.assertEqual(self.employee_1.get_cpr_number(), "2103981529")

    def test_get_phone(self):
        self.assertEqual(self.employee_1.get_phone(), "23957361")

    def test_set_phone(self):

        self.employee_1.set_phone("23957362")
        self.assertEqual(self.employee_1.get_phone(), "23957362")

    def test_get_email(self):
        self.assertEqual(self.employee_1.get_email(), "w.charels.devlin@gmail.com")

    def test_set_email(self):

        self.employee_1.set_email("w.charels.devlin1@gmail.com")
        self.assertEqual(self.employee_1.get_email(), "w.charels.devlin1@gmail.com")

    def test_get_age(self):
        self.assertEqual(self.employee_1.get_age(), 24)

if __name__ == "__main__":
    unittest.main()

