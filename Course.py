class Course:

    def __init__(self, course_id: str, course_name: str, course_responsible: str):
        self.__course_id: str = course_id
        self.__course_name: str = course_name
        self.__course_responsible: str = course_responsible

    def __str__(self):
        return f"Course ID: {str(self.__course_id)}, Course name: {str(self.__course_name)}," \
               f" Course responsible: {str(self.__course_responsible)}, Course Location:  "

    def set_course_responsible(self, new_course_responsible: str):
        self.__course_responsible = new_course_responsible

    def get_course_responsible(self):
        return self.__course_responsible

    def get_course_id(self):
        return self.__course_id

    def get_course_name(self):
        return self.__course_name