# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 19:02:01 2016

@author: jakubmalcharczyk
"""

import pandas as pd
import seaborn
import matplotlib.pyplot as plt
import numpy as np
pd.set_option('display.max_columns',None)
data = pd.read_csv('gapminder.csv',low_memory =False)
data['incomeperperson']=data['incomeperperson'].convert_objects(convert_numeric=True).dropna()
data['urbanrate']=data['urbanrate'].convert_objects(convert_numeric=True).dropna()
data['polityscore']=data['polityscore'].convert_objects(convert_numeric=True).dropna()
plt.figure()
seaborn.distplot(data['incomeperperson'].dropna(), kde=False)
plt.savefig('incomeperpeson.pdf')
#plt.clf()
plt.figure()
seaborn.distplot(data['urbanrate'].dropna(),kde=False)
plt.savefig('urbanrate.pdf')
plt.figure()
seaborn.distplot(data['polityscore'].dropna(), kde=False)
plt.savefig('polityscore.pdf')
plt.figure()
seaborn.regplot(x='incomeperperson', y='polityscore', fit_reg=False, data=data)
plt.savefig('democracy.pdf')