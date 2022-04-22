from datetime import date, time
from CourseLocation import CourseLocation
from Course import Course

class CourseRequest:
    request_id = 0

    def __init__(self, course: Course, course_date: date, course_time: time, course_location: CourseLocation):
        self.__course = course
        self.__course_date = course_date
        self.__course_time = course_time

        self.__course_location = course_location
        CourseRequest.request_id += 1

    def __str__(self):
        return f"Request: {str(self.request_id)}, course, {str(self.__course)}," \
               f" date: {str(self.__course_date)}, time: {str(self.__course_time)}," \
               f" location, {str(self.__course_location)}"

    def check_available_time(self, course_time: time, set_course_time):
        if course_time == set_course_time:
            return False
        else:
            return True

    def set_course_date(self, course_date: date): self.__course_date = course_date

    def get_course_date(self):
        return self.__course_date

    def set_course_time(self, course_time: time):
        self.__course_time = course_time

    def get_course_time(self):
        return self.__course_time

    def set_course_location(self, course_location: CourseLocation):
        self.__course_location = course_location

    def get_course_location(self):
        return self.__course_location

