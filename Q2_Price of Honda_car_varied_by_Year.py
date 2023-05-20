# -*- coding: utf-8 -*-
"""
Created on Sun May  7 09:43:05 2023

@author: manim
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('clean_honda_sell_data_new.csv')
df = df.loc[df['Condition'] == 'Used']

# Group the data by 'Condition' and 'Year' columns and calculate the mean price
condition_car = df.groupby(['Condition', 'Year'])['Price'].mean().reset_index()

# Filter the data to skip the years between 2007 and 2009
condition_car = condition_car[~condition_car['Year'].isin(range(2007, 2010))]

# Create a figure with one subplot
fig, ax = plt.subplots(figsize=(10, 6))

# Plot a line graph of the mean price over year based on the condition
sns.lineplot(data=condition_car, y='Price', x='Year', hue='Condition', ax=ax)

# Add numeric points to the plot
sns.scatterplot(data=condition_car, y='Price', x='Year', hue='Condition', ax=ax, 
                marker='o', s=100, edgecolor='black', linewidth=1.5)

# Set the plot title and axis labels
ax.set(title="Price over year based on the condition", xlabel="Year", ylabel="Price")

# Add values for the numeric points
for line in range(0,condition_car.shape[0]):
     ax.annotate(round(condition_car['Price'].iloc[line], 2), 
                 xy=(condition_car['Year'].iloc[line],condition_car['Price'].iloc[line]),
                 xytext=(10,-5), textcoords='offset points')

# Show the plot
plt.show()