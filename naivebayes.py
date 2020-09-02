# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 00:36:59 2020

@author: Sajal
"""
import pandas as pd
import numpy as np
#Import scikit-learn dataset library
#from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
#Import scikit-learn metrics module for accuracy calculation
from sklearn import metrics
import matplotlib.pyplot as plt



#Load dataset
wine = pd.read_csv('Wine_data.csv', sep= ',', header = 0)
# print the names of the 13 features
print ("Features: ", wine.shape)

# print the label type of wine(class_0, class_1, class_2)
print ("Labels: ", wine.columns)
# print data(feature)shape
print(wine.shape)

print (wine.head())
print (wine)

X = wine.values[:, 1:5] 
Y = wine.values[:, 0]
# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2,random_state=109) # 70% training and 30% test

#Create a Gaussian Classifier
gnb = GaussianNB()

#Train the model using the training sets
gnb.fit(X_train, y_train)

#Predict the response for test dataset
y_pred = gnb.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",(metrics.accuracy_score(y_test, y_pred)*100))
plt.plot(y_pred)
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()