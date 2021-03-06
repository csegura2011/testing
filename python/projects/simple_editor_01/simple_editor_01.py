# -*- coding: utf-8 -*-

# File: simple_editor_01.py
# Author:
# Creation Date: 2017/April/05

# References
# - https://www.binpress.com/tutorial/building-a-text-editor-with-pyqt-part-one/143




import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt



class Main(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.initUI()
    def initUI(self):
        # x and y coordinates on the screen, weight, height
        self.setGeometry(100,100,1030,800)
        self.setWindowTitle("Writer")

def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()





