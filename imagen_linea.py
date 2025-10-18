# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 22:28:28 2025

@author: Carlos Gil
"""

import matplotlib.pyplot as plt
import numpy as np

img = np.zeros((256, 256))


n_lineas= 20
puntos_linea=10

    
for i in range(n_lineas):
    x= np.int32(np.linspace(0, 50, puntos_linea))
    y= np.int32(np.linspace(0, 100, puntos_linea))
    plt.plot(np.random.uniform(x, y, puntos_linea))
   


plt.show()    
    