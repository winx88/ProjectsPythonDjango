#-*- coding: utf-8 -*-
'''
Created on 06-04-2012

@author: Piotr Zagórski
'''
import random

class mRSA(object):
    '''
    Obliczanie modułu RSA
    '''

    def __init__(selfparams):
        '''
        Constructor
        '''        
    # funkcja licząca NWD z liczb a i b
    def nwd(self,a, b):
        while b:
            a, b = b, a%b
        return a
    
    # funkcja obliczajaca ciąg bi i={0...n}
    # jeśli jednak bi!=1 po przejściu n kroków
    # funkcja zwraca -1 i przechodzimy do ponownego 
    # losowania
    def bi(self,b,n):
        bi = [0]*2
        bi[0] = b
        for i in range(n):
            bi[1] = pow(bi[0],2,n)
            if bi[1] == 1:
                if bi[0] == n-1:
                    bi[0] = -1
                    bi[1] = -1
                    return bi
                else:
                    return bi
            bi[0] = bi[1]
        bi[0] = -1
        bi[1] = -1
        return bi    
    
    # funkcja obliczająca rozkład modułu RSA jako tablice pq
    def distRSA(self,n,d,e):
        s = 0
        t = 0
        b = 0 
        a = 0
        ed = e*d-1
        pq = [0]*2
        
        # liczymy t oraz s spełniajace warunek ed-1 = 2^s * t
        while ed % 2 == 0:
                ed = ed / 2
                s=s+1
        t = ed
        
        while(1):
            # losujemy liczby z przedziału od 2 do n      
            a = random.randrange(2,n)
            a2 = self.nwd(a,n)
            # jesli mielismy szczescie to trafiliśmy w dobre a2
            # więc mamy odrazu rozkład modułu 
            if(a2!=1):
                pq[0] = a2
                pq[1] = n/a2
                return pq
            else:
                b = pow(a, t, n)
                if b != 1:
                    # liczymy ciąg bi
                    tempbi = self.bi(b,n)
                    # jeśli tempbi[0] == -1 oznacza to ze w ciągu bi, bi!=1
                    # więc przystępujemy do ponownego losowania 
                    if(tempbi[0]!=-1):
                        pq[0] = self.nwd(n, tempbi[0]-1)
                        pq[1] = n/pq[0]
                        return pq
            
m = mRSA()
print 'Obliczanie rozkładu modułu RSA...'
print m.distRSA(71033,47071,331)
print 'KONIEC'


        
