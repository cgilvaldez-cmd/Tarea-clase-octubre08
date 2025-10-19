# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 22:28:28 2025

@author: Carlos Gil
"""

import matplotlib.pyplot as plt
import numpy as np
import random as r 

img = np.zeros((256, 256))

    
for i in range(20):
    x1= r.randint(0, 100)
    y1= r.randint(0, 100)
    x2= r.randint(0, 100)
    y2= r.randint(0, 100)

    plt.plot([x1, y1], [x2, y2])

plt.show()    
    