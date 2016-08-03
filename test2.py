# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 18:58:05 2016

@author: jakubmalcharczyk
"""

#Import libraries.
import pandas as pd
import numpy as np
#Read in data.
data = pd.read_csv('marscrater_pds.csv', low_memory = False)
#Give frequency counts and percentage for 3 variables.
diam = data['DIAM_CIRCLE_IMAGE']
bins = np.linspace(diam.min(), diam.max(), 10)
c1 = diam.groupby(pd.cut(diam, bins)).size()
p1 = c1*100 / len(diam)
print('Frequency count for the diameter of the craters.')
print(c1)
print('Percentages for the diameter of the craters.')
print(p1)
depth = data['DEPTH_RIMFLOOR_TOPOG']
bins = np.linspace(depth.min(), depth.max(), 10)
c2 = depth.groupby(pd.cut(depth, bins)).size()
p2 = c2*100 / len(depth) 
print('Frequency count for the depth of the craters.')
print(c2)
print('Percentages for the depth of the craters.')
print(p2)
num_layers = data['NUMBER_LAYERS']
c3 = depth.groupby(num_layers).size()
p3 = c3*100 / len(num_layers) 
print('Frequency count for the number of layers in each crater.')
print(c3)
print('Percentages for the number of layers in each crater.')
print(p3)