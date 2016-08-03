# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 22:12:38 2016

@author: jakubmalcharczyk
"""
import pandas
data = pandas.read_csv('gapminder.csv', low_memory = False)
print(len(data))
print(len(data.columns))
data['incomeperperson'] = data['incomeperperson'].convert_objects(convert_numeric=True)
d1 = data['incomeperperson'].dropna()
ic1 = (d1).mean()
print('Income per person mean is equal')
print(ic1)
pic1 = d1>=ic1
print ("Percentages how many countries have Income per person higher or equal to mean")
pic1 = pic1.value_counts(sort=False, normalize = True)
print (pic1)

data['urbanrate']= data['urbanrate'].convert_objects(convert_numeric=True)
d2 = data['urbanrate'].dropna()
ic2 = (d2).mean()
print ('Urban rate mean is equal:')
print(ic2)
print ('Percentages how many countries have Urban rate higher or equal to mean')
pic2 = d2>=ic2
pic2 = pic2.value_counts(sort=False, normalize =True)
print (pic2)

data['polityscore']=data['polityscore'].convert_objects(convert_numeric = True)
d3= data['polityscore'].dropna()
ic3 = (d3).mean()
print('Polity score mean is equal:')
print (ic3)
print ("Percentages how many countries have Polity score higher or equal to mean")
pic3 = d3>=ic3
pic3 = pic3.value_counts(sort=False, normalize =  True)
print (pic3)
