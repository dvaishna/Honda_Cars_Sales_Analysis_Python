#!/usr/bin/env python
# coding: utf-8

# In[92]:


import os
import pandas as pd
import numpy as np
from IPython.display import display
import scipy.stats as stats

current_directory = os.getcwd()

in_file_name = "C:\\MSIS\\CIS_5270\\Python\\Project\\code\\clean_honda_sell_data.csv"

# Reading the csv file into dataframe
df_file = pd.read_csv(in_file_name, encoding='utf-8')


# Getting the total rows & columns
print("-------------- Total Rows & Columns ----------------")
display(df_file.shape)

# Some General info about the dataframe
print("-------------- General info ----------------")
display(df_file.info())

# Some basic statistical characteristics of each numerical columns
pd.set_option('display.max_columns', None)

stats_num = df_file[['Price', 'Consumer_Rating', 'Mileage']].describe() # Compute the descriptive statistics
styled_stats = stats_num.style.format("{:.2f}") # Create a Styler object and apply formatting
print("-------------- Statistics on Numerical datatypes ----------------")
display(styled_stats) # Display the formatted statistics


# statistics on non-numerical datatypes
print("-------------- Statistics on Non-Numerical datatypes ----------------")
stats_obj = df_file[['Model', 'Condition', 'Drivetrain', 'Fuel_Type', 'Transmission', 'State']].describe(include=["object"]) # Compute the descriptive statistics
display(stats_obj) # Display the statistics


# -------------- Max values of each numeric columns ----------------
# Select the numerical columns
num_cols = df_file.select_dtypes(include=np.number)

# Apply np.max to the numerical columns
print("-------------- Max values of each numeric columns ----------------")
max_values = num_cols.apply(np.max)
display(max_values.to_frame().style.format("{:.2f}"))


# -------------- Group by Model, Statistics shown of - Price ----------------
print("-------------- Group by Model, Stats - Consumer Ratings ----------------")
# group the data and compute summary statistics, including only groups with at least 2 observations
grouped_stats = df_file.groupby(["Model"])["Price"].agg(lambda x: [np.size(x), np.mean(x), np.std(x), np.min(x), np.max(x)] if len(x) >= 2 else [])

# drop any empty rows resulting from the filter
grouped_stats = grouped_stats[grouped_stats.apply(lambda x: len(x) > 0)]

# convert the results to a DataFrame and apply column names
grouped_stats = pd.DataFrame(grouped_stats.tolist(), index=grouped_stats.index, columns=["count", "mean", "std", "min", "max"])

# format the results and display as a styled table
display(grouped_stats.style.format("{:.2f}"))


# -------------------- Skewness on Consumer Rating ---------------
print("-------------------- Skewness on Consumer Rating ---------------")

filtered_df = df_file[(df_file['Year'] >= 2021) & (df_file['Year'] <= 2023)]

# group the DataFrame by "Condition" and calculate the skewness of "Value_For_Money_Rating"
skewness = filtered_df.groupby(["Condition"])["Value_For_Money_Rating"].apply(lambda x: stats.skew(x))

# create a new DataFrame to display the results
summary_df = pd.DataFrame({'Skewness': skewness})

display(summary_df)


# -------------- Contigency table with Model & condition ----------------
print("-------------- Contigency table with Model & condition ----------------")
display(pd.crosstab(df_file["Model"], df_file["Condition"]).style.format("{:.2f}"))



# In[ ]:




