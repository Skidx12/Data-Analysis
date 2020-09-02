# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 11:25:20 2019

@author: Sajal
"""
#DATA CLEANING BY BINNING METHOD

from scipy import stats
import itertools
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

df = pd.read_csv('Wine_data.csv')

saved_column = df.Alcohol;

row_no = int(input('enter the number of rows:'))
id1 = 0
list_col = []

for row in itertools.islice(saved_column,0,row_no):
    list_col.append(row)
    print(id1,'           ',row)
    id1+=1;
array = np.array(list_col)
print("Array : ",array)
print('            ')
array = np.sort(array)
print('The Sorted array is:')
print(array)
print('\nSelect: \n1: Bin by mean \n2:Bin by Median \n3: Bin by Mode \n4: Bin by  Border:')

in1 = int(input())
if(in1 == 1):
    bin_1 = []
    bin_2 = []
    bin_3 = []
    print('-----------------------Bin by mean---------------------')
#    array.sort()
    inbin = int(input('Enter the number of bins:'))
    if (len(array)%inbin != 0):
        print('Invalid Bin Number')
    bins = np.split(array,inbin)
    print(bins)
    mean1 = np.mean((bins[0]))
    for x in bins[0]:
        bin_1.append(mean1)
    print('\n1st Bin:')
    print(bin_1)
    mean2 = np.mean((bins[1]))
    for x in bins[1]:
        bin_2.append(mean2)
    print('\n2nd Bin:')
    print(bin_2)
    mean3 = np.mean((bins[2]))
    for x in bins[2]:
        bin_3.append(mean3)
    print('\n3rd Bin:')
    print(bin_3)
if(in1 == 2):
    bin_1 = []
    bin_2 = []
    bin_3 = []
#    array.sort()
    print("-----------------------Bin by median---------------------")
    inbin = int(input('Enter the number of bins:'))
    if (len(array)%inbin != 0):
        print('Invalid Bin Number')
    bins = np.split(array,inbin)
    print(bins)
    med1 = np.median(bins[0])
    for x in bins[0]:
        bin_1.append(med1)
    print('\n1st Bin:')
    print(bin_1)
    med2 = np.median((bins[1]))
    for x in bins[1]:
        bin_2.append(med2)
    print('\n2nd Bin:')
    print(bin_2)
    med3 = np.median((bins[2]))
    for x in bins[2]:
        bin_3.append(med3)
    print('\n3rd Bin:')
    print(bin_3)


if(in1 == 3):
    bin_1 = []
    bin_2 = []
    bin_3 = []
#    array.sort()
    print('-----------------------Bin by mode---------------------')
    inbin = int(input('Enter the number of bins:'))
    if (len(array)%inbin != 0):
        print('Invalid Bin Number')
    bins = np.split(array,inbin)
    print(bins)
    mod1 = stats.mode(bins[0])
    for x in bins[0]:
        bin_1.append(mod1)
    print('1st Bin:')
    print(bin_1)
    mod2 = stats.mode((bins[1]))
    for x in bins[1]:
        bin_2.append(mod2)
    print('2nd Bin:')
    print(bin_2)
    mod3 = stats.mode((bins[2]))
    for x in bins[2]:
        bin_3.append(mod3)
    print('3rd Bin:')
    print(bin_3)
if(in1 == 4):
    print('-----------------------Bin by Border---------------')
    bin_1 = []
    bin_2 = []
    bin_3 = []
#    array.sort()
    inbin = int(input('Enter the number of bins:'))
    if (len(array)%inbin != 0):
        print('Invalid Bin Number')
    bins = np.split(array,inbin)
    print(bins)
    min1 = min(bins[0])
    max1 = max(bins[0])
    for x in bins[0]:
        if((x - min1) < (max1 - x)):
            bin_1.append(min1)
        else:

            bin_1.append(max1)
    print('1st Bin:')