# -*- coding: utf-8 -*-
"""
Created on Sat May  6 16:33:27 2023

@author: manim
"""


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('clean_honda_sell_data_new.csv')


# Group the data by 'Condition' column and count the number of entries in each group
condition_counts = df.groupby('Condition')['Price'].count()
colors = ['#0077c2', '#8dc6f7', '#b7d9f1']

# Create a pie chart of the car distribution based on condition
plt.pie(condition_counts, labels=condition_counts.index, autopct='%1.1f%%', startangle=90, colors= colors)
plt.title('Car Distribution by Condition')
plt.show()