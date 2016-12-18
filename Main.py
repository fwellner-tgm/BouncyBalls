"""
Author: Florian Wellner
Date: 18.12.2016
Exercise: Balls that fly across the window and bounce off the walls

Help from: Markus Reichl
"""

import sys
from Controller import Controller
from PySide import QtGui


class App(QtGui.QApplication):
    def __init__(self):
        """
        Initializes the app and creates an control instance
        """
        super().__init__(sys.argv)
        self.control = Controller()

        while self.control.view.isVisible():
            self.control.view.update()
            self.processEvents()

        sys.exit()

if __name__ == '__main__':
    app = App()
    app.exec_()