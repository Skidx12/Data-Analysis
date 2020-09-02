# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 12:48:50 2020

@author: Sajal
"""

import pandas as pd
import numpy as np
import pyfpgrowth

df = pd.read_csv('Wine_data.csv')
df = df.head(100)
# initialize list of lists 
#data = [['Apple,Orange,Grape'], ['Apple,Orange'],['Mango,Pineapple,Papaya'],['Apple,Papaya'],['Grape,Orange,Pineapple']] 
  
# Create the pandas DataFrame 
#df = pd.DataFrame(data, columns = ['Transaction ID', 'Items']) 
"""
Products_list = df.values.tolist()
#print(Products_list)

val=int(input("Enter the Minimum Support Count :"))

patterns = pyfpgrowth.find_frequent_patterns(Products_list,val)
print("Patterns with Minimum support of ",val," are displayed as follows..")
print(patterns)


"""


import pandas as pd
import numpy as np
import pyfpgrowth

df = pd.read_csv('Wine_data.csv')

#df = df.drop('ID', axis=1)

#df = df.TRANSACTION

#df=df.tolist()

print("Data Set :",df)
Products_list = df.values.tolist()
df = [line.split(',') for line in df]

print("Individual Items : ",df)

"""val=int(input("Enter the Minimum Support Count :"))
patterns = pyfpgrowth.find_frequent_patterns(df, val)
"""
val=int(input("Enter the Minimum Support Count :"))

patterns = pyfpgrowth.find_frequent_patterns(Products_list,val)
print("Patterns with Minimum support of ",val," are displayed as follows..")
print("\n",patterns)
#print("Expected patterns :",patterns)

print("\nConclusion \nThe item with the maximum confidence is usually mixed together for the preparation of Wine.")