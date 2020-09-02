# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:44:12 2019

@author: Sajal
"""

"""
        DATA TRANSFORMATION

"""
import itertools      
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('X:\#PADHAI LIKHAII\Semester 4\Data mining Lab\Wine_data.csv')
#print(df)
print('----------------Z score Transformation----------------------')
saved_column = input('Enter Column Name:')
saved_column = df.Alcohol
print('Cultivator:    Alcohol content:')   
row_no = 30
id1 = 0
for row in itertools.islice(saved_column,1,row_no):
    print(id1,'           ',row)
    id1+=1; 
array = np.array(saved_column)
print(array)
"""transform = preprocessing.scale(array)
print(transform)"""
print('\n\nThe Z values for every data are:')
for x in array:
    a1 = [[x - np.mean(array)]/np.std(array)]
    print(a1)
saved_column.plot(x='Id', y='Alcohol', kind='density')
plt.show()
print('\n\n--------------------Min and Max for data---------------------')
saved_column1 = input('Enter Column Name:')
saved_column1 = df.Alcohol
print('ID:    Alcohol content:')   
row_no = 30
id1 = 0
for row in itertools.islice(saved_column,1,row_no):
    print(id1,'           ',row)
    id1+=1;
mini = min(saved_column1)
maxi = max(saved_column1)
print('    ')
print('The minimum Alcohol is:',mini)
print('The maximum Alcohol is:',maxi)
print('\n\n---------------------------------Alcohol in a given range---------------------')
saved_column2 = input('Enter Column Name:')
saved_column2 = df.Alcohol
l1 = int(input('Enter lower range:'))
l2 = int(input('Enter upper range:'))
print('Alcohol level in given range are:')
array_petal = np.array(saved_column2)
array_petal.sort()
for x in array_petal:
    if(x > l1 and x < l2):
        print(x)
saved_column2.plot(x='Id', y='Alcohol', kind='density') 
