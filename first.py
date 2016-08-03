# my first program on this course
import pandas
import numpy

data = pandas.read_csv('gapminder.csv',low_memory=False)
print(len(data)) #Number of observation (rows)
print(len(data.columns)) #Number of observation (columns)

c1= data["incomeperperson"]#.value_counts(sort=False)
print(c1)

p1= data["incomeperperson"].value_counts(sort=False, normalize=True)
print(p1)