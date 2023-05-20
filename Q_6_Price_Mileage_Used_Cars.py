# -*- coding: utf-8 -*-
"""
Created on Sat May  6 18:58:03 2023

@author: dvaishn2
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



in_file_name = "C:\\MSIS\\CIS_5270\\Python\\Project\\code\\clean_honda_sell_data.csv"

# Reading the csv file into dataframe
df_file = pd.read_csv(in_file_name, encoding='utf-8')

# Set color palette
my_palette = sns.color_palette("Blues")

# Filter the data for used cars with condition column value as "used"
used_cars = df_file[df_file['Condition'] == 'Used']

# Filter the data for years between 2021 to 2023
filtered_cars = used_cars[(used_cars['Year'] >= 2021) & (used_cars['Year'] <= 2023)]

# Create the density plot
sns.kdeplot(data=filtered_cars, x='Mileage', y='Price', hue='Year', fill=True, palette='Blues')

# Set labels and title
plt.xlabel('Mileage')
plt.ylabel('Price')
plt.title('Density plot of Mileage and Price for Used Cars (2021-2023)')