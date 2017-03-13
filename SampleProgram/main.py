# From https://www.baldengineer.com/raspberry-pi-gui-tutorial.html 
# by James Lewis (@baldengineer)
# Minimal python code to start PyQt5 GUI
#

# always seem to need this
import sys

# This gets the Qt stuff
import PyQt4
from PyQt4.QtWidgets import *

from PyQt4 import QtCore, QtGui

# This is our window from QtCreator
import mainwindow_auto

from PyALPR import PlateReader

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow_auto.Ui_MainWindow):
    # access variables inside of the UI's file

    ### functions for the buttons to call
    def pressedOnButton(self):
        print ("Pressed On!")
        image = QtGui.QImage("alpr.jpg")
        self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))
        reader = PlateReader();
	reader.read_plate();
	self.LPRlabel.setText(reader.plate)

    def pressedOffButton(self):
        print ("Pressed Off!")

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file

        ### Hooks to for buttons
        self.btnOn.clicked.connect(lambda: self.pressedOnButton())
        


# I feel better having one of these
def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())

# python bit to figure how who started This
if __name__ == "__main__":
    main()
