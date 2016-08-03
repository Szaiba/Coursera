# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 15:26:49 2016

@author: jakubmalcharczyk
"""

import pandas
data = pandas.read_csv('gapminder.csv', low_memory=False)
data['incomeperperson'] = pandas.to_numeric(data['incomeperperson'], errors='coerce')
data['lifeexpectancy'] = pandas.to_numeric(data['lifeexpectancy'], errors='coerce')
data['urbanrate'] = pandas.to_numeric(data['urbanrate'], errors='coerce')
print('counts for income per person divided in 10 ranges')
income_groups = pandas.cut(data['incomeperperson'], 10).value_counts(sort=False)
print (income_groups)
print('counts for expected lifetime divided in 5 ranges')
lifeexpectancy_groups = pandas.cut(data['lifeexpectancy'], 5).value_counts(sort=False)
print(lifeexpectancy_groups)
print('counts for rate of urbanization divided in 5 ranges')
urbanrate_groups = pandas.cut(data['urbanrate'], 5).value_counts(sort=False)
print (urbanrate_groups)