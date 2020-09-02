# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 09:46:53 2019

@author: Vikash
"""

# -*- coding: utf-8 -*-
import pandas as pd
import array
import itertools
import numpy as np
import statistics

def bin():
   
    filename = str(input("Which file do you want?"))
    if not ".csv" in filename:
        filename += ".csv"
        file=pd.read_csv(filename)


    print("COLUMN NAMES \n")
    l=file.columns.values
    c=0
    for i in file:
        c=c+1
        print(c, "-" , i)

    colname=int(input("ENTER ID OF COLUMN :"))
    targetcol=file[l[colname-1]]
    #Selected_column = file[colname]
    print("SELECTED COLUMN :",l[colname-1])
    
    n=targetcol.count()
    print("NUMBER OF DATA", n)
    
    if type(targetcol.iloc[0]) == str:
        print("THIS FUNCTION CAN BE APPLIED ON INTEGER TYPE ONLY ")
        return
    
    row_no = n
    id1 = 0
    list_col = []
    

    for row in itertools.islice(targetcol,0,row_no):
        list_col.append(row)
        id1+=1;
    array = np.array(list_col)

    array = np.sort(array)
    print("\nTHE SORTED ARRAY IS:")
    print("\n",array)   
    
    old_min=array.min()
    old_max=array.max()
    
    print("\nBin",":","[MIN: ",old_min,", MAX: ",old_max,"]")
    #print("\nEnter number of ROWS: ")
    row_no = int(input("\nEnter number of ROWS: "))
    print('S.No.           ',l[colname-1],' Content')   
    id1 =0
    for i in range(0,row_no):
        print(i,"           ",targetcol[i])
    
    print('    ')
    print('The minimum ',l[colname-1],' is:',old_min)
    print('The maximum ',l[colname-1],' is:',old_max)
    
    print("\n")
    print("Enter new Min : ")
    new_min=int(input())
    print("Enter new Max : ")
    new_max=int(input())
    ID = 0
    print("\n\n********************Data Transformation********************")
    print('S.No.           ',l[colname-1],' Content')
    co=0
    for i in array:
        
        saved_column1 = (i-old_min)/(old_max-old_min)*(new_max-new_min)+new_min
        ID+=1
        print(ID,"           ",round(saved_column1,4))
        co=co+1
        if co == row_no:
            break
          
bin()

    

        
        

