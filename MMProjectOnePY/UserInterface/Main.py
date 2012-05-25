'''
Created on 13-05-2012

@author: winx
'''

import sys
from PyQt4 import QtGui
from MainWindow import *


def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 