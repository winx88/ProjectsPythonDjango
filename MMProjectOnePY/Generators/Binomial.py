# -*- coding: utf-8 -*-
'''
Created on 09-05-2012

@author: winx
'''
from math import factorial
from numpy import *
from numpy.random import *
from UserInterface.CheckInput import CheckInput

class Binomial(object):
    '''
    Generator dwumianowy
    '''

    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.name = 'Rozkład dwumianowy'
   
    def getN(self):
        return self.n
    
    def getP(self):
        return self.p
    
    def getName(self):
        return self.name       
    
    def randomFromUniform(self,sample):
        '''
        losowanie z próbki
        '''
        length=len(sample)
        if length==2:
            return uniform(low=sample[0], high=sample[1])
        else:
            return sample[int(round(uniform(low=0, high=length-1)))]
        
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
        
    def binomialCoefficient(self, n, k):
        '''
        Oblicza dwumian Newtona
        '''    
        return factorial(n) // (factorial(k) * factorial(n - k))

    def probabilityChart(self, X):
        '''
        Oblicza współrzedne wykresy prawdopodobienstwa
        '''  
        #TODO: jeśli jest jeden elemnt to sie sypie i jesli jest wiecej jak liczyc      
        g = []
        for l in X:
            P = self.binomialCoefficient(self.n, l) * pow(self.p[0], l) * pow((1 - self.p[0]), (self.n - l))
            g.append(P)
        return g
    #TODO: generownie losowe p
    def generateInt(self, k):
        '''
        generuje k liczb rozkładu dwumianowego        
        '''
        T = (self.n+1) * [0]       
        for l in range(k): # k generownych liczb
            prob = self.randomFromUniform(self.p)
            X = 0
            for i in range(self.n): #  n prób
                U = uniform(low=0, high=1)
                if U <= prob:
                    X = X + 1
            T[X] = T[X] + 1                
        return T



 
