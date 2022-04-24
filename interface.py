from PyQt6 import QtWidgets, uic
from PyQt6.QtGui import QAction
import sys

from Course import Course
from CourseLocation import CourseLocation
from CourseRequest import CourseRequest
from datetime import date, time


class CourseRequestGUI(QtWidgets.QMainWindow):

    def __init__(self):
        super(CourseRequestGUI, self).__init__()
        uic.loadUi("CRGUI.ui", self)

        self.submitbtn.clicked.connect(self.submit_button_pressed)
        self.exitbtn.clicked.connect(self.exit_button_pressed)
        self.clearbtn.clicked.connect(self.clearbtn_pressed)

        self.show()

    def clearbtn_pressed(self):
        line_edits = self.findChildren(QtWidgets.QLineEdit)
        for field in line_edits:
           field.clear()


    def exit_button_pressed(self):
        self.close()

    def submit_button_pressed(self):
        course = self.course_field.text()
        courseDate = self.coursedate_field.text()
        courseTime = self.coursetime_field.text()
        courseLocation = self.courselocation_field.text()

        course = course.split(",")
        courseDate = courseDate.split(",")
        courseTime = courseTime.split(",")
        courseLocation = courseLocation.split(",")

        courseID = course[0].strip()
        courseName = course[1].strip()
        courseResponsible = course[2].strip()

        coursedateyear = int(courseDate[0])
        coursedatemonth = int(courseDate[1])
        coursedateday = int(courseDate[2])

        coursetimehour = int(courseTime[0])
        coursetimeminute = int(courseTime[1])

        courselocationid = courseLocation[0].strip()
        courselocationaddress = courseLocation[1].strip()

        course1 = Course(courseID, courseName, courseResponsible)

        courselocation1 = CourseLocation(courselocationid, courselocationaddress)
        coursedate1 = date(coursedateyear, coursedatemonth, coursedateday)
        coursetime1 = time(coursetimehour, coursetimeminute)

        courserequest = CourseRequest(Course(courseID, courseName, courseResponsible),
                                      date(coursedateyear, coursedatemonth, coursedateday),
                                      time(coursetimehour, coursetimeminute),
                                      CourseLocation(courselocationid, courselocationaddress))

        courserequestreturnmsg = f"{course1}, {courselocation1}, Date: {coursedate1}, Time: {coursetime1}"
        self.showresult.setText(f"{courserequestreturnmsg}")