import sys
from Controller import Controller
from PySide import QtGui


if __name__ == "__main__":
    #the window
    app = QtGui.QApplication(sys.argv)

    c = Controller()

    #as long as the window ist visible, it is being repainted
    while c.view.isVisible():
        c.view.update()
        #needs to be included or the windows freezes
        app.processEvents()

    #should quit the program when the programm is closed but is kind of does not work
    sys.exit(app.exec_())