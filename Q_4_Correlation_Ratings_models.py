# -*- coding: utf-8 -*-
"""
Created on Sat May  6 15:46:23 2023

@author: dvaishn2
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt



in_file_name = "C:\\MSIS\\CIS_5270\\Python\\Project\\code\\clean_honda_sell_data.csv"

# Reading the csv file into dataframe
df_file = pd.read_csv(in_file_name, encoding='utf-8')

# Calculate the mean ratings by car model
mean_ratings = df_file.groupby('Model')[['Comfort_Rating', 'Interior_Design_Rating', 'Performance_Rating', 'Value_For_Money_Rating', 'Exterior_Styling_Rating', 'Reliability_Rating']].mean()

# Get the top 5 models based on overall rating
top_models = mean_ratings.mean(axis=1).sort_values(ascending=False)[:3].index

# Filter the data to only include the top 5 models
df_top = df_file[df_file['Model'].isin(top_models)]

# Create a facet grid
g = sns.FacetGrid(data=df_top, height=4)

# Map a scatter plot of consumer rating vs number of reviews for each model
g.map(sns.scatterplot, x='Consumer_Rating', y='Consumer_Review_#', hue='Model', palette='mako', data=df_top)
g.add_legend()

# Set the axis labels and title
g.set_axis_labels('Consumer Rating', 'Consumer_Review_#')
g.fig.suptitle('Relationship between Consumer Rating and Number of Reviews for Top 3 Car Models', fontsize=16, y=1.05)

# Adjust the spacing between the plots
g.tight_layout()

# Show the plot
plt.show()