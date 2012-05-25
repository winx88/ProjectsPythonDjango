# -*- coding: utf-8 -*-
'''
Created on 19-05-2012

@author: winx
'''

from math import factorial
from numpy import *
from numpy.random import *
from numpy.ma.core import floor, log, exp
from HistogramPlot.PlotHist import PlotHist

 
class Poisson(object):
    '''
    Generator Poissona
    '''

    def __init__(self,lamb):
        self.lamb = lamb 
        self.name = 'Rozkład poissona'
    
    def getlambda(self):
        return self.lamb
    
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
            P = exp(-self.lamb)*(pow(self.lamb,l)/factorial(l))
            g.append(P)
        return g
        
    
    def generateInt(self, k):
        '''
        generowanie k liczb
        '''
        T = [0]*k        
        for i in range(k):
            q = exp(-self.lamb)
            X = -1
            S = 1
            while S > q:
                U = uniform(low=0, high=1)
                S = S*U
                X = X + 1
            T[X] = T[X] + 1
        return T
    
    
#A = Poisson(30)
#C = A.showIntGenAndCount(A.generateInt(1000)) 
#P = A.probabilityChart(C)        
#A = PlotHist()
#A.plotHistgram("Generator dwumianowy", C,P,1,'ilosc','liczby')
#A.showHistogram()
