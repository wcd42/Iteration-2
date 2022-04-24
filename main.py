import sys
from PyQt6 import QtWidgets
from interface import CourseRequestGUI

app = QtWidgets.QApplication(sys.argv)
main_window = CourseRequestGUI()
app.exec()
