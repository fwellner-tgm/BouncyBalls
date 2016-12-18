"""
Author: Florian Wellner
Date: 18.12.2016
Exercise: Balls that fly across the window and bounce off the walls

Help from: Markus Reichl
"""

from PySide.QtGui import *
from PySide.QtCore import *


class View(QWidget):
    """
    Represents the GUI
    """

    width = 420
    height = 350
    radius = 3

    def __init__(self):
        """
        Contructor
        """
        #calling the base class
        super().__init__()

        self.setupUi()

        #array for the point processes
        self.points = []

    def setupUi(self):
        """
        Defines how the GUI looks like
        :return:
        """

        self.width = View.width
        self.height = View.height

        #height and width of the buttons
        self.b_width = 170
        self.b_height = 28

        #a painter required to paint/draw
        self.painter = QPainter()

        #title of the window
        self.setWindowTitle("POINTS!!!")

        #object name of the class
        self.setObjectName("Form")

        #size of the window, not resizable
        self.setFixedSize(self.width, self.height)

        #a stylesheet which uses CSS commands
        self.setStyleSheet("QWidget#Form {background-color: white} "
                           "QPushButton {font-size: 13px}")

        #2 buttons
        self.new = QPushButton(self)
        self.remove = QPushButton(self)

        #name of the buttons
        self.new.setObjectName("new")
        self.remove.setObjectName("remove")

        #text that is displayed on the buttons
        self.new.setText("New point")
        self.remove.setText("Remove Last Point")

        #moves the buttons to the the given location
        self.new.move(self.width/100 * 28 - self.b_width/2, self.height/100 * 88)
        self.remove.move(self.width/100 * 72 - self.b_width/2, self.height/100 * 88)

        #sets the size of the buttons
        self.new.resize(self.b_width, self.b_height)
        self.remove.resize(self.b_width, self.b_height)

        #displays the buttons
        self.new.show()
        self.remove.show()

    def paintEvent(self, event):
        """
        A method required to paint
        :param event:
        :return:
        """
        #new pen
        mypen = QPen()

        #the thickness of the pen
        mypen.setWidth(10)
        #color of the pen
        mypen.setColor(Qt.blue)

        #everythng between painter.begin and painter.end will be painted and displayed
        self.painter.begin(self)
        #sets the custom pen to the painter
        self.painter.setPen(mypen)
        #paints the list
        for point in self.points:
            self.painter.drawEllipse(point.x.value, point.y.value, 3, 3)

        self.painter.end()

    def closeEvent(self, event):
        """
        Method that is called when the window is closed
        :param event:
        :return:
        """

        #join every process in the list
        for p in self.points:
            p.join()

        event.accept()
