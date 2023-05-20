# -*- coding: utf-8 -*-
"""
Created on Sat May  6 20:47:00 2023

@author: dvaishn2
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

in_file_name = "C:\\MSIS\\CIS_5270\\Python\\Project\\code\\clean_honda_sell_data.csv"

# Reading the csv file into dataframe
df_file = pd.read_csv(in_file_name, encoding='utf-8')

new_cars = df_file[(df_file['Condition']=='New') & (df_file['Year']>=2021) & (df_file['Year']<=2023)]

# Create pivot table
heatmap_data = pd.pivot_table(new_cars, values='Price', index='Fuel_Type', columns='Condition', aggfunc=np.mean)

# Create heatmap
sns.set(style='white')
cmap = sns.color_palette("Blues", as_cmap=True)
ax = sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap=cmap)

# Set title and labels
ax.set_title('Price variations based on Fuel Type for new cars from 2021 to 2023')
ax.set_xlabel('Condition')
ax.set_ylabel('Fuel Type')
plt.show()
