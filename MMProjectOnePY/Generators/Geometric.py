# -*- coding: utf-8 -*-
'''
Created on 19-05-2012

@author: winx
'''
from numpy import *
from numpy.random import *
from numpy.ma.core import floor, log
from HistogramPlot.PlotHist import PlotHist

 
class Geometric(object):
    '''
    Generator geometryczny
    '''

    def __init__(self,p):
        self.p = p
        self.name = 'Rozkład geometryczny'
    
    def getP(self):
        return self.p
    
    def getName(self):
        return self.name       
      
        
    def showIntGenAndCount(self,list):
        '''
        wypisuje liste wylosowanych liczb
        '''
        R = []
        index = 0
        for i in list:
            if i != 0:
                for l in range(i):
                    R.append(index)
            index=index+1
        return R
                              
    def probabilityChart(self, X):
        '''
        y dla wykresu prawdopodobienstwa
        '''
        g = []
        for l in X:
            P = self.p*(pow(1-self.p,l))
            g.append(P)
        return g
    
    def generateInt(self, k):
        '''
        generowanie k liczb
        '''
        T = [0]*k
        for i in range(k):
            U = uniform(low=0, high=1)
            X = log(U)/log(1-self.p)
            T[(int(floor(X)))] = T[(int(floor(X)))] + 1
        return T
            
            
#A = Geometric(0.1)
#C = A.showIntGenAndCount(A.generateInt(100)) 
#P = A.probabilityChart(C)        
#A = PlotHist()
#A.plotHistgram("Generator dwumianowy", C,P,1,'ilosc','liczby')
#A.showHistogram()