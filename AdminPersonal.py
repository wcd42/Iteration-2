from Employee import Employee

class AdminPersonel(Employee):

    def __init__(self, institute_id, course_request: list):
        self.institute_id = institute_id
        self.course_request = course_request