# -*- coding: utf-8 -*-
"""
Created on Sat May  6 17:32:58 2023

@author: dvaishn2
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


in_file_name = "C:\\MSIS\\CIS_5270\\Python\\Project\\code\\clean_honda_sell_data.csv"

# Reading the csv file into dataframe
df_file = pd.read_csv(in_file_name, encoding='utf-8')

# Create a boolean mask for "New" cars
mask = df_file['Condition'] == 'New'

# Filter the DataFrame using the mask
df_file = df_file[mask]

# Define a custom color palette
custom_palette = ['#044B7F', '#1C758A', '#29A0B1', '#9CD9E6']

# Create subplots for Price vs. Milage, Price vs. Transmission, and Price vs. Powertrain
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))

# Subplot 1: Price vs. Transmission
sns.boxplot(x='Transmission', y='Price', data=df_file, ax=axes[0], palette='Blues')
axes[0].set_xlabel('Transmission')
axes[0].set_ylabel('Price')
axes[0].set_title('Price variations based on transmission')

# Subplot 2: Price vs. Powertrain
sns.boxplot(x='Drivetrain', y='Price', data=df_file, ax=axes[1], palette='Blues')
axes[1].set_xlabel('Drivetrain')
axes[1].set_ylabel('Price')
axes[1].set_title('Price variations based on Drivetrain')


# Show the plot
plt.show()

# Adjust the spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()