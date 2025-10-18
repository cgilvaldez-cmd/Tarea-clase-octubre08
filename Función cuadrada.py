# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 20:50:33 2025

@author: Carlos Gil
"""

import matplotlib.pyplot as plt
import numpy as np

def f(X):
    return X**2

def df(X):
    return 2*X
    
h= 0.1
x = np.arange(-1, 4, h)
y = x**2
x0=1
y0= f(x0)
m = df(x0)

def tangent(x):
    return m * (x-x0) + y0

tangente = tangent(x)    


plt.plot(x, y, 'blue')
plt.plot(x, tangente, 'red')

plt.show()

    