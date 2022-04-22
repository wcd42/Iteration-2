class CourseLocation:

    def __init__(self, location_id: str, address: str):
        self.__location_id: str = location_id
        self.__address: str = address

    def __str__(self):
        return f"Location ID: {str(self.__location_id)}, Address: {str(self.__address)}"

    def get_address(self):
        return self.__address

    def set_address(self, new_address):
        self.__address = new_address

