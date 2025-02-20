# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 14:16:49 2025

@author: RJJohnson
"""

import pandas as pd

# Load the training data
train_data = pd.read_csv('train_FD001.txt', sep=" ", header=None)
train_data.drop(columns=[26, 27], inplace=True)  # Drop unused columns

# Add column names (based on dataset documentation)
column_names = [
    'id', 'cycle', 'setting1', 'setting2', 'setting3', 
    's1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 
    's11', 's12', 's13', 's14', 's15', 's16', 's17', 's18', 's19', 
    's20', 's21'
]
train_data.columns = column_names

# Display the first few rows
print(train_data.head())