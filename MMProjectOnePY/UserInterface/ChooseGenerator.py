# -*- coding: utf-8 -*-
'''
Created on 17-05-2012

@author: winx
'''
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from UserInterface.CheckInput import CheckInput
from Generators.Binomial import Binomial
from HistogramPlot.PlotHist import PlotHist
from UserInterface.ExceptionInput import ExceptionInput
try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class ChooseGenerator(QWidget):
    '''
    classdocs
    '''


    def __init__(self,parent = None):
        '''
        Constructor
        '''
        QWidget.__init__(self, parent)
        self.initUI()
        
    def initUI(self): 
        
                
        
        QLabel('Dane dla generatora:',self).move(20,55)
        
        QLabel('n > 1 : ',self).move(95,90)        
        
        self.n = QLineEdit(self)
        self.n.move(170,85)      
        
        QLabel('0 < p < 1 : ',self).move(95,120)       
        
        self.p = QLineEdit(self)
        self.p.move(170,115)
        
        QLabel('losowe p : ',self).move(95,145)
        randP = QCheckBox(self).move(168,145)   
        
        QLabel('k > 0 : ',self).move(95,173)
             
        
        self.k = QLineEdit(self)
        self.k.move(170,168)       
        
        
        genbut = QPushButton('Generuj',self)
        
        genbut.move(330,180)
        self.connect(genbut, SIGNAL("clicked()"),self.generateHist)
        
        #TODO: QMessageBox('NIEEEEEEEE').show()
    def generateHist(self):
        p = []
        k,n = 0,0
        chkval = CheckInput()
        flaga = False
        try:
            if int(self.n.text()) <= 1:
                msg = QMessageBox(self)
                msg.setInformativeText(_fromUtf8('Wartość p jest mniejsza lub równa 1'))
                msg.setText(_fromUtf8('Ostrzeżenie !'))
                msg.setWindowTitle('   ')
                
                msg.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                msg.setFixedSize(300,300)            
                msg.exec_()
                print 'niepoprawna wartosc jedynak'
                return
            else:
                n = int(self.n.text())
        except ValueError:
            print 'niepoeprwna wartość 1'
            return
            
        try:
            st = str(self.p.text())
            for s in st.split(","):
                p.append(float(s))
                try:
                    chkval.checkValueIsSection(p)
                except ExceptionInput:
                    print 'wartosc z poza zakresu'
                    return
                
        except ValueError:
            print 'niepoprawna wartosc 2'
            return
            
        try:
            if int(self.k.text()) <= 1:
                print 'niepoprawna wartosc jedynak'
                return
            else:
                k = int(self.k.text())
        except ValueError:
            QMessageBox(self).show()            
            print 'niepoeprwna wartość 3'
            return
            
        flaga = True
        if flaga == True:           
            B = Binomial(n,p)
            C =B.showIntGenAndCount(B.generateInt(k)) 
            P = B.probabilityChart(C)        
            A = PlotHist()
            A.plotHistgram("Generator dwumianowy", C,P,1,'ilosc','liczby')
            A.showHistogram()



        