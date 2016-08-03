# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 21:54:50 2016

@author: jakubmalcharczyk
"""

import pandas as pd
import numpy
import seaborn
import matplotlib.pyplot as plt

data = pd.read_csv('addhealth_pds.csv', low_memory=False)
print(len(data))

data['H1DA4']=data['H1DA4'].replace(6,numpy.nan)
data['H1DA4']=data['H1DA4'].replace(8,numpy.nan)
data['H1DA5']=data['H1DA5'].replace(6,numpy.nan)
data['H1DA5']=data['H1DA5'].replace(8,numpy.nan)
data['H1DA6']=data['H1DA6'].replace(6,numpy.nan)
data['H1DA6']=data['H1DA6'].replace(8,numpy.nan)
sub1=data[['H1DA4','H1DA5','H1DA6']]
sub1=sub1.convert_objects(convert_numeric=True)
print(sub1.describe(percentiles=True))
def MOTHER (row):
    if row ['H1WP17A']>=1:
        return 1
    if row ['H1WP17B']>=1:
       return 2
    if row ['H1WP17C']>=1:
        return 3
    if row ['H1WP17D']>=1:
        return 4
    if row ['H1WP17E']>=1:
       return 5
    if row ['H1WP17F']>=1:
        return 6
    if row ['H1WP17G']>=1:
       return 7
    if row ['H1WP17H']>=1:
        return 8
    if row ['H1WP17I']>=1:
        return 9
    if row ['H1WP17J']>=1:
       return 10
    if row ['H1WP17K']>=1:
        return 11
data['MOTHER']= data.apply(lambda row: MOTHER(row), axis=1)
gr2 = data.groupby("MOTHER").size()
gr2.rename(index={'1':'bla1','2' :'bla2'})
print(gr2*100/len(data))
def FATHER (row):
    if row ['H1WP18A']>=1:
        return 1
    if row ['H1WP18B']>=1:
       return 2
    if row ['H1WP18C']>=1:
        return 3
    if row ['H1WP18D']>=1:
        return 4
    if row ['H1WP18E']>=1:
       return 5
    if row ['H1WP18F']>=1:
        return 6
    if row ['H1WP18G']>=1:
       return 7
    if row ['H1WP18H']>=1:
        return 8
    if row ['H1WP18I']>=1:
        return 9
    if row ['H1WP18J']>=1:
       return 10
    if row ['H1WP18K']>=1:
        return 11
data['FATHER']=data.apply(lambda row: FATHER(row), axis=1)
gr3 = data.groupby("FATHER").size()
print (gr3*100/len(data))
sub3 = [gr2,gr3]
sub4=gr2+gr3
sub4=sub4.convert_objects(convert_numeric=True)
print (pd.crosstab(gr2,gr3))
gr3['FATHER']=data['FATHER'].astype('category')
seaborn.countplot(x="FATHER",data=gr3)
plt.xlabel('xlabel Title')
plt.title('Title')
