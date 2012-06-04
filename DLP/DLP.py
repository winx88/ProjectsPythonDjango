# -*- coding: utf-8 -*-
'''
Created on 21-05-2012

@author: Piotr Zagórski
'''
from math import sqrt, ceil 

class DLP(object):
    '''
    Problem logarytmu dyskretnego
    '''


    def __init__(self):
        pass
    
    def checkIndex(self, q, N): 
        r = N % q
        if r == 1 or r == 0:
            r1 = (N - r) % q
            if r == 1 or r == 0:
                return -1
        else:
            return r
        
    def distributionOfPrime(self, p):
        '''
        Rozkład liczby na czynniki pierwsze
        '''
        ptab = [2, 3, 5, 7, 11, 13 , 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]
        p1 = p - 1
        distp = {}
        for i in ptab:
            count = 1
            while p1 % i == 0:
                distp[i] = count
                count = count + 1 
                p1 = p1 / i
        distp[p1] = 1
        return distp
    
    def isGenerator(self,generator,p,distributionOfp):
        '''
        Sprawdza czy dana liczba jest generatorem
        '''
        p1 = p-1
        for pi in distributionOfp.iterkeys():
            if pow(generator,(p1/pi),p)!= 1:
                return True
        return False
    
    def extgcd(self,u, v):
        '''
        Oblicza rozszerzony alfa i beta w rozszerzonym algorytmie 
        Euklidesa
        u3 => NWD(u,v)
        u * u1 + v*u2 = NWD(u,v)
        '''
        u1 = 1
        u2 = 0
        u3 = u
        v1 = 0
        v2 = 1
        v3 = v
        while v3 != 0:
            q = u3 / v3
            t1 = u1 - q * v1
            t2 = u2 - q * v2
            t3 = u3 - q * v3
            u1 = v1
            u2 = v2
            u3 = v3
            v1 = t1
            v2 = t2
            v3 = t3
        return u1, u2, u3
    
    def algorithmShanks(self,g,q,n):
        '''
        Obliczanie problemu logarytmu dyskretnego algorytmem Shanksa
        g^x = q mod n
        n => modulo
        g => g^x
        q => g^x = q
        return x
        '''
        smallSteps = {} # tablica malych krokow
        giantSteps = {} # wielkich kroków
        m = ceil(sqrt(n-1))
        for a in range(int(m)):
            smallSteps[a] = (pow(g, a,n))
        smallSteps[int(m)] = (pow(g, int(m),n))
        
        smallStepsSorted = smallSteps.items()
        smallStepsSorted.sort(key=lambda x: x[1])
        u1, reverseItem, nwd = self.extgcd(n, smallSteps[int(m)])
        
        for i in range(int(m)):
            giantSteps[i] = (q* pow(reverseItem, i,n)) % n
            for h in smallStepsSorted:
                if h[1] >= giantSteps[i]:  
                    if h[1] == giantSteps[i]:
                        return h[0] + i*int(m)
    
    def algorithmHellmana(self,g,q,p):
        '''
        Przeprowadza redukcje hellmana a nastepnie oblicza x z crt 
        '''
        distP = self.distributionOfPrime(p)
        moduls = [] # moduly
        smallDlp = {} # rozkład na miejszcze dlp
        cong = {} # układ kongruencjii
        x = [] # x ze składowych dlp
        
        for k in distP.iterkeys():
            moduls.append(pow(k,distP[k]))
    
        for m in range(len(moduls)):
            smallDlp[(pow(g,moduls[m]*moduls[(m+1)%len(moduls)]))%p] = (pow(q,moduls[m]*moduls[(m+1)%len(moduls)]))%p
            x.append(self.algorithmShanks((pow(g,moduls[m]*moduls[(m+1)%len(moduls)]))%p, smallDlp[(pow(g,moduls[m]*moduls[(m+1)%len(moduls)]))%p], p))
        
        cong[x[2]]=moduls[1]
        cong[x[1]]=moduls[0]
        cong[x[0]]=moduls[2]
        
        #print 'Układ kongruencjii',cong
        #print 'Małe problemy DLP',smallDlp
        return self.solveCong(cong)   
         
    def solveCong(self,modrest):
        '''
        Oblicza układ trzech kongruencji
        '''
        
        modul = []
        rest = []        
        
        for m in modrest.iterkeys():
            modul.append(modrest[m])
            rest.append(m)
    
        k1 = 0
        k2 = 0
        
        for k in range(modul[1]):
            temp = (modul[0]*k + rest[0]) % modul[1]
            if  temp == rest[1]:
                k1 = k
        for k in range(modul[2]):
            temp = ((modul[0]*k1 + rest[0]) + modul[0]*modul[1]*k) % modul[2]
            if temp == rest[2]:
                k2 = k
                
        return ((modul[0]*k1 + rest[0]) + modul[0]*modul[1]*k2)    
            
                    
A = DLP()
print 'Sprawdzamy możliwość zwolnienia dla liczb: 47353, 229749'
if A.checkIndex(47353, 229749) != -1:
    print '...niestety nie udało się :( wynik to', A.checkIndex(47353, 229749)
else:
    print 'udało się nie robimy nic dalej:P'
print 'Sprawdzamy czy ', 5, ' jest generatorem grupy ', 47353
print 'Przeprowadzamy rozkład liczby ',47353,' na iloczyn liczb pierwszych'
print A.distributionOfPrime(47353)
print 'Sprawdzamy czy liczba ',5,'generuje grupę multyplikatywną Z*',47353
print 'Odpowiedź brzmi:',A.isGenerator(5, 47353, A.distributionOfPrime(47353))
print 'Przeprowadzamy redukcje Hellmana mamy 3DLP dla 5^x = 229749 mod 47353 '
print '44076^x = 44076 mod 47353'
print '11204^x = 30416 mod 47353'
print '7446^x =  39906 mod 47353'
print 'Co daje nam układ kongruencji: '
print  'x = 1 mod 8'
print  'x = 2 mod 3'
print  'x = 1665 mod 1973'
print 'Z czego otrzymujemy wynik:'
print A.algorithmHellmana(5,229749,47353)
print 'KONIEC' 

