'''
Created on 14-05-2012

@author: winx
'''

class ExceptionInput(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)