# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 14:55:55 2025

@author: RJJohnson
"""

from Python_file import train_data

# Fill missing values with the mean
train_data.fillna(train_data.mean(), inplace=True)

from sklearn.preprocessing import MinMaxScaler

# Normalize sensor data
scaler = MinMaxScaler()
sensor_columns = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9', 's10', 
                  's11', 's12', 's13', 's14', 's15', 's16', 's17', 's18', 's19', 's20', 's21']
train_data[sensor_columns] = scaler.fit_transform(train_data[sensor_columns])

print(train_data.head())

# Group by engine ID and calculate RUL
train_data['RUL'] = train_data.groupby('id')['cycle'].transform(lambda x: x.max() - x)

print(train_data[['id', 'cycle', 'RUL']].head())

# Features (X)
X = train_data.drop(columns=['id', 'RUL'])

# Target (y)
y = train_data['RUL']

print(X.head())
print(y.head())

from sklearn.model_selection import train_test_split

# Split data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

print(X_train.shape, X_val.shape)