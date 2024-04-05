# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 14:54:15 2024

@author: basti
"""

import numpy as np
import numpy.linalg as l 

n= 10
T = range(100)


nu = np.log(n)/len(T)

w = np.array([1 for i in range(n)])

c = [0 for i in T]
y_bar = [0 for i in T]



for i in T:
    c[i] = (w/sum(w))
    y_bar[i] = FP(c[i],p[i])
    if  y_bar[i] == y[i]:
        z = 0
    else:
        z = (y_bar[i]-y[i])/l.norm(y_bar[i]-y[i], -np.inf)
    w = w -nu(w @ z)
    
    
    
    
