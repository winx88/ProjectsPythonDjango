# -*- coding: utf-8 -*-

'''
Created on 13-05-2012

@author: winx
'''
from UserInterface.ChooseGenerator import ChooseGenerator
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class MainWindow(QMainWindow):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        super(MainWindow, self).__init__()
        self.initUI()
        
    def initUI(self):
        
        
        change = QLabel('Wybierz generator: ',self)
        change.resize(200,20)
        change.move(20,20)
        
        self.combo = QComboBox(self)
        self.combo.move(170,15)
        self.combo.resize(200,30)
        self.combo.addItem('-------------')        
        self.combo.addItem('Dwumianowy')
        self.combo.addItem('Geometryczny')
        self.combo.addItem('Poissona')
        self.combo.addItem('Wykladniczy')
        self.combo.addItem('Pareto')
        self.combo.addItem('Logistyczny')
        self.combo.addItem('Normalny')
         
        self.setGeometry(300, 300, 450, 230)
        self.setWindowTitle('Generatory liczb losowych')
        self.setWindowIcon(QIcon('Random.png'))
        self.show()
        
        self.connect(self.combo, SIGNAL("activated(int)"), self.onActivated)
        
        
           
        
    def onActivated(self, text):
        if(text == 1):
            box = ChooseGenerator(self) 
            self.setCentralWidget(box)
        if(text == 2):
            self.centralWidget().deleteLater()
                    
        
        
        
     
        
