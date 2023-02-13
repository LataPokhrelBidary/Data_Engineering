#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 10:45:36 2022

@author: latabidary
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.linear_model import LinearRegression

data = pd.read_excel('data.xlsx')

X= data.iloc[:,1].values.reshape(-1,1)
Y= data.iloc[:,0].values.reshape(-1,1)

linear_regressor = LinearRegression()
linear_regressor.fit(X, Y)
Y_pred = linear_regressor.predict(X)

plt.scatter(X, Y)
plt.plot(X, Y_pred,color='red')
plt.show()
