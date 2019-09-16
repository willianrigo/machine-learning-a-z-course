# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Data Preprocessing

#Importing the libraries

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
dataset = pd.read_csv('Data.csv')

#iloc: select all [rows, columns]
# ':' --> all rows/columns
# ':-1' all rows/columns except the last one
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values


#taking care of missing data
#
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN',
                  strategy = 'mean',
                  axis=0)

#we want second and third column
#so use 1:3 because the last number
#is exlusive

imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])