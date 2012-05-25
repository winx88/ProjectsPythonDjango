# -*- coding: utf-8 -*-
'''
Created on 14-05-2012

@author: winx
'''

from UserInterface.ExceptionInput import ExceptionInput

class CheckInput(object):
        
    def __init__(self):
        pass
    
    def checkValueIsInt(self,val):
        if round(val)!= val:
            raise ExceptionInput("Value is not integer")
    
    def checkValueIsNegative(self, val):
        if type(val).__name__=='int':
            if not val >= 0:
                raise ExceptionInput("Value is negative")
        else:
            for v in val:
                if not v >= 0:
                    raise ExceptionInput("Value is negative")
        
    def checkValueIsSection(self, val, set=[0, 1]):
        for v in val:
            if  not set[0] > v and not v < set[1]:
                raise ExceptionInput("Value is not section")

    def checkValueIsDifferent(self,val):
        sortedTab = sort(val)
        for i in range(len(sortedTab)):
            if sortedTab[i]==sortedTab[(i+1)%len(sortedTab)]:
                raise ExceptionInput("Values is not different in array") 
            