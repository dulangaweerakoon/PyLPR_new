# From https://www.baldengineer.com/raspberry-pi-gui-tutorial.html 
# by James Lewis (@baldengineer)
# Minimal python code to start PyQt5 GUI
#

# always seem to need this
import sys

# This gets the Qt stuff
import PyQt4
#from PyQt4.QtWidgets import *

from PyQt4 import QtCore, QtGui, uic

# This is our window from QtCreator
form_class = uic.loadUiType("mainwindow.ui")[0]

from PyALPR import PlateReader

# create class for our Raspberry Pi GUI
class MainWindow(QtGui.QMainWindow, form_class):
    # access variables inside of the UI's file

    ### functions for the buttons to call
    def pressedOnButton(self):
        reader = PlateReader();
        reader.read_plate();
        self.LPRlabel.setText(reader.plate + "")
        print (reader.plate + "")
        image = QtGui.QImage("alpr.jpg")
        self.imageLabel.setPixmap(QtGui.QPixmap.fromImage(image))
        
	
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
    app = QtGui.QApplication(sys.argv)
    form = MainWindow()
    form.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())

# python bit to figure how who started This
if __name__ == "__main__":
    main()
