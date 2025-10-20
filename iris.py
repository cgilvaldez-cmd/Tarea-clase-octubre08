# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 22:32:36 2025

@author: Carlos Gil
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

datos = pd.read_csv('iris.csv')

print(datos)

datos.boxplot()

datos.hist()

datos.plot()

plt.show()