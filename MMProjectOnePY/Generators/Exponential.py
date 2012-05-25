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

 
class Exponential(object):
    '''
    Generator wykładniczy
    '''

    def __init__(self,lamb):
        self.lamb = lamb 
        self.name = 'Rozkład wykładniczy'
    
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
        y dla wykresu gestosci
        '''
        #TODO : jak jest z ta funkcją harakterystyczną
        for x in X:
            P = self.lamb*exp(-self.lamb*x)
        
    
    def generateInt(self, k):
        '''
        generowanie k liczb
        '''
        T = [0]*k        
        for i in range(k):
            U = uniform(low=0, high=1)
            X = - log(U)/self.lamb
            T.append(X)
        return T
    
A = Exponential(20)
print A.generateInt(10)