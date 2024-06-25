"""Exploring a regression dataset that is based off salary amounts based on years worked using EDA.

This dataset is found on https://www.kaggle.com/code/ybifoundation/simple-linear-regression
EDA means Exploritory Data Analyisis."""


import pandas as pd
import matplotlib.pyplot as plt

# Importing dataset.
salary = pd.read_csv('https://github.com/ybifoundation/Dataset/raw/main/Salary%20Data.csv')

# Exploring the feature of years of experience.
X = salary["Experience Years"]
print(type(X))
print(len(X))
print(dir(X))

# Exploring the feature of salary amounts in U.S. dollars.
y = salary["Salary"]
print("")
print(type(y))
print(len(y))
print(dir(y))

# Creating a scatter plot for the dataset.
plt.scatter(X,y,c=y)
plt.xlabel("Years Working")
plt.ylabel("Salary Amount($)")
plt.title("Salary amount based on years worked")
plt.grid()
plt.colorbar()
