#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 11:51:27 2020

@author: king
"""

# importing important libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
dataset = pd.read_csv('Social_Network_Ads.csv')
x=dataset.iloc[:,2:4].values
y=dataset.iloc[:,4].values

#spliting the data into training set and test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0) 

# feature scaling
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
sc_y=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test=sc_y.fit_transform(x_test)

# Support vector classification
from sklearn.svm import SVC
classifier=SVC(kernel='linear',random_state=0)
classifier.fit(x_train,y_train)

#testing of classification model
y_pred=classifier.predict(x_test)

#creating confusion matrix to check how many prediction are correct or not
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

