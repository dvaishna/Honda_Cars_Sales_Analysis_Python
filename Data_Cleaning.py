# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 14:44:52 2023

@author: dvaishn2
@author: manim
"""


import os
import pandas as pd
import numpy as np

current_directory = os.getcwd()

in_file_name = "honda_sell_data.csv"

# Construct the full file path using the os module
in_file_path = os.path.join(current_directory, in_file_name)
# op_file_path = os.path.join(directory_path, op_file_name)


# Reading the csv file into dataframe
df_file = pd.read_csv(in_file_path, encoding='utf-8')

# print(df_file.head())
# print(df_file.dtypes)

# replacing "-" with nan
df_file = df_file.replace({"–": np.nan})

# ----------- Cleaning Year Column ------------
df_file['Year'] = pd.to_datetime(df_file['Year'], format='%Y').dt.year


# ----------- Cleaning Price Column ------------
df_file["Price"] = pd.to_numeric(df_file["Price"].str.replace("[^\d\.]+", "", regex= True), errors="coerce")


def average_price():
    avg_prices = df_file.groupby("Model")["Price"].mean()
    null_prices = df_file["Price"].isna()
    df_file.loc[null_prices, "Price"] = df_file.loc[null_prices, "Model"].map(avg_prices)
    
average_price()

# ----------- Cleaning Drivetrain Column ------------

df_file['Drivetrain'] = df_file['Drivetrain'].str.lower()
df_file['Drivetrain'] = df_file['Drivetrain'].str.replace('front-wheel drive', 'fwd', regex=True)
df_file['Drivetrain'] = df_file['Drivetrain'].str.replace('all-wheel drive|four-wheel drive', 'awd', regex=True)
df_file['Drivetrain'] = df_file['Drivetrain'].str.replace('rear-wheel drive', 'rwd', regex=True)


# ----------- Cleaning Transmission Column ------------
# dropping rows containing null values in Transmission column
df_file = df_file.dropna(subset = ['Transmission'])


# define a dictionary mapping transmission types to standardized values
transmission_dict = {
    'automatic': ['automatic', 'a/t', '9-speed', 'variable', 'driver selectable mode'],
    'manual': ['manual', 'm/t'],
    'cvt': ['cvt']
}

# convert transmission strings to lowercase
df_file['Transmission'] = df_file['Transmission'].str.lower()

# map transmission types to standardized values using dictionary
for key, value in transmission_dict.items():
    transmission_regex = '|'.join(value)
    df_file.loc[df_file['Transmission'].str.contains(transmission_regex, regex=True), 'Transmission'] = key

# handle specific case where Transmission contains 'other' and Model contains 'CR-V'
df_file.loc[(df_file['Transmission'].str.contains('other')) & (df_file['Model'].str.contains('CR-V')), 'Transmission'] = 'cvt'

# set any remaining 'other' transmissions to 'automatic'
df_file.loc[df_file['Transmission'].str.contains('other'), 'Transmission'] = 'automatic'

# drop raws with invalid transmissions
df_file = df_file[~df_file['Transmission'].str.contains('cylinder')]
df_file = df_file[~df_file['Transmission'].str.contains('2')]

# ----------------------- Cleaning Milage column ------------------

df_file["Mileage"] = df_file["Mileage"].str.replace("BluetoothUSB", "USB", regex=False)

# Define the list of strings to replace with NaN
replace_list = ["USB", "Premium", "HomeLinkRear", "Alloy", "BluetoothUSB", "Apple"]

# Replace the strings in the Mileage column with NaN
for item in replace_list:
    df_file["Mileage"] = df_file["Mileage"].str.replace(item, "99.99", regex=False)
    
# Convert the Mileage column to float
df_file["Mileage"] = df_file["Mileage"].astype(float)


# Replace the values 99.99 with NaN
df_file["Mileage"] = df_file["Mileage"].replace(99.99, np.nan, regex=False)

# Replace all NaN values with mean

# Calculate the mean of each column
means = round(df_file['Mileage'].mean(),0)

# Replace NaN values with mean values
df_file['Mileage'].fillna(means, inplace=True)


# ---------------------------- cleaning Rating columns -------------------

# Calculating median values for all 6 rating types columns based on the car models
def diff_ratings_median():
    rating_types = ['Comfort_Rating', 'Interior_Design_Rating', 'Performance_Rating', 'Value_For_Money_Rating', 'Exterior_Styling_Rating', 'Reliability_Rating']
    for rating_type in rating_types:
        average_rating_type_car_model = df_file.groupby("Model")[rating_type].median()
        null_rating_type_rows = df_file[df_file[rating_type].isna()][["Model", rating_type]]
        for index, row in null_rating_type_rows.iterrows():
            model = row['Model']
            df_file.at[index, rating_type] = average_rating_type_car_model[model]
            

diff_ratings_median()

# --------------- cleaning MPG column ------------

df_file[['min_MPG', 'max_MPG']] = df_file['MPG'].str.split("–", expand=True).astype(float)
df_file.drop('MPG', axis=1, inplace=True)
df_file[['min_MPG', 'max_MPG']] = df_file[['min_MPG', 'max_MPG']].replace(0.0, np.nan)

def fill_missing_mpg():
    for mpg_col in ['min_MPG', 'max_MPG']:
        avg_mpg_by_model = round(df_file.groupby('Model')[mpg_col].mean(),2)
        null_mpg_rows = df_file[mpg_col].isna()
        df_file.loc[null_mpg_rows, mpg_col] = df_file.loc[null_mpg_rows, 'Model'].map(avg_mpg_by_model)

fill_missing_mpg()      

# ---------------- Dropping rows with NaN as values ----------

df_file.drop(df_file[(df_file['State']=='MO-22') | (df_file['State']=='Route') | (df_file['State']=='Glens')].index, inplace=True)
df_file =df_file.dropna(subset=['State','Seller_Type','Exterior_Color','Drivetrain','Mileage', 'min_MPG', 'max_MPG','Comfort_Rating', 'Interior_Design_Rating', 'Performance_Rating', 'Value_For_Money_Rating', 'Exterior_Styling_Rating', 'Reliability_Rating' ]).drop_duplicates()


df_file.to_csv('clean_honda_sell_data.csv', index=False)

