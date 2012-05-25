# -*- coding: utf-8 -*-
'''
Created on 13-05-2012

@author: winx
'''

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from Generators.Binomial import Binomial
from numpy import *
from numpy.random import *


class PlotHist(object):
    '''
    Uniwersalna klasa do rysowania histogramów
    '''

    #TODO: U uniwersalinić na dyskretny i ciągly i dla duzych wartosci uporzdkować osie:)
    def __init__(self):
        pass
            
    def plotHistgram(self,nameOfGen,listOfGen,listOfProbValue,distOrCont,desX,desY):
        '''
        nameOfGen = nazwa generatora
        listOfGen = lista wygenerowanych liczb
        listOfProbValue = lista wartość do krzywej
        distOrCont = dyskretny lub ciągły
        desX = opis osi X
        desY = opis osi Y
        '''
        # opis
        plt.xlabel(desX)
        plt.ylabel(desY)
        plt.title('Histogram: '+nameOfGen)
        # jesli bedzie ciagly to zaminst 0.5 odejmujemy 1 chyba:P
        
        n, bins, patches = plt.hist(listOfGen, bins=np.arange(min(listOfGen),max(listOfGen)+2,1)-.5, normed=1 ,facecolor='green',alpha=0.85)
        plt.plot(listOfGen, listOfProbValue, 'r--', linewidth=1)         
        plt.autoscale()# automatyczne skalowanie osi
        plt.grid(True)
        
        plt.xticks(range(len(self.generateLabel(bins))), self.generateLabel(bins), size='small')
        
    def generateLabel(self,bins):
        label = []
        for i in range(int(round(bins[len(bins)-1]+3))):
            label.append(str(i))
        return label
    
    def showHistogram(self):
        plt.show()
        
        
  
        
#B = Binomial(40,[0.5])
#C =B.showIntGenAndCount(B.generateInt(10000)) 
#P = B.probabilityChart(C)        
#A = PlotHist()
#A.plotHistgram("Generator dwumianowy", C,P,1,'ilosc','liczby')
#A.showHistogram()
        

            
