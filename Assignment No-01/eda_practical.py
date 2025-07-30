import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import date

# Load dataset
data = pd.read_csv('used_cars_data.csv')

# Basic info
print(data.head())
print(data.tail())
print(data.info())
print(data.describe())
print(data.nunique())
print(data.isnull().sum())
print((data.isnull().sum() / len(data)) * 100)

# Data Reduction
data = data.drop(['S.No.'], axis=1)
print(data.info())

# Feature Engineering
data['Car_Age'] = date.today().year - data['Year']
print(data[['Year', 'Car_Age']].head())

# Creation of new features
data['Brand'] = data.Name.str.split().str.get(0)
data['Model'] = data.Name.str.split().str.get(1).fillna('') + data.Name.str.split().str.get(2).fillna('')
print(data[['Name', 'Brand', 'Model']].head())

print("Unique Brands:", data.Brand.unique())
print("Number of Unique Brands:", data.Brand.nunique())

searchfor = ['Isuzu', 'ISUZU', 'Mini', 'Land']
print("Filtered Brands (Isuzu, Mini, Land):")
print(data[data.Brand.str.contains('|'.join(searchfor))].head(5))
