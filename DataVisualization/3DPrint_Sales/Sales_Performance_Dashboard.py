import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
import os
import pandas as pd
import requests
import streamlit as st

# Get current working directory
cwd = os.getcwd()
# Using the absolute path, point to the sales csv
csv_file = os.path.join(cwd,"cults3D_sales.csv")
# convert the csv file into a dataframe
df = pd.read_csv(csv_file)
# make the country codes all upper case
df['countryCode'] = df['countryCode'].str.upper()
# remove the time and convert the purchase timestamp strings to a date type
df['saleDate'] = df['saleDate'].str.split("T").str[0]
# make the dates appear as purely date with no time stamp
df['saleDate'] = pd.to_datetime(df['saleDate']).dt.date
# convert the cost into cents
df['cost'] = df['cost']/100
# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

st.header("Nerdboy_Q Cults3D Sales", divider=True)
st.write(df)

col1, col2 = st.columns((2,2))

# ==============================Data by Design Country=========================
col1.subheader("Popularity by Country")
# group data by country for country stats
country_groups = df.drop(columns=['countryCode','design','saleDate','user']).groupby('country')
# get the download count per country
country_count_df = country_groups.count().reset_index()
# get the purchase total by country 
country_buyer_df = country_groups.sum().reset_index()
# join the count and purchase totals by country into one dataframe
country_df = country_count_df.merge(country_buyer_df, left_on='country', right_on='country')
# clean up old objects
del country_groups
del country_count_df
del country_buyer_df

country_df = country_df.rename(columns={'cost_x': 'total sales', 'cost_y':'total revenue'})
col1.write(country_df)

# ==============================Data by Design Popularity=========================
col2.subheader("Popularity by Design")
# group data by design for country stats
design_groups = df.drop(columns=['country','countryCode','saleDate','user']).groupby('design')
# get the download count per design
design_count_df = design_groups.count().reset_index()
# get the purchase total by design 
design_buyer_df = design_groups.sum().reset_index()
# join the count and purchase totals by design into one dataframe
design_df = design_count_df.merge(design_buyer_df, left_on='design', right_on='design')
# rename the columns for clean data review
design_df = design_df.rename(columns={'cost_x':'total downloads', 'cost_y':'total revenue'})
# clean up old objects
del design_groups
del design_count_df
del design_buyer_df

col2.write(design_df)

# ==============================Sales by Country Pie Chart=========================
country_pi, ax0 = plt.subplots()
patches, labels, autotext = ax0.pie(
    country_df['total sales'],
    autopct="%1.1f%%",
    labels=country_df['country'],
    shadow=True,
    wedgeprops={'alpha':0.5}
) 
ax0.axis('equal')

# Set the pie chart labels to white
for i, text in enumerate(labels):
    lbl = labels[i].get_text()
    val = float(autotext[i].get_text()[:-1])
    # if value less than 5% of sales, hide the
    # chart label & value for better visibility
    if val < 3:
        # print("-", lbl, val)
        labels[i].set_visible(False)
        autotext[i].set_visible(False)
    else: 
        labels[i].set_color('white')
        autotext[i].set_color('white')
        # text.set_color(patches[i].get_facecolor())

# set chart background transparent
country_pi.set_facecolor('none')
# display country popularity pie chart in the 2nd column
col1.pyplot(country_pi)

# ==============================Sales by Design Pie Chart=========================
design_pi, ax1 = plt.subplots()
patches, labels, autotext = ax1.pie(
    design_df['total downloads'],
    autopct="%1.1f%%",
    labels=design_df['design'],
    shadow=True,
    wedgeprops={'alpha':0.5}
) 
ax1.axis('equal')
# plt.title(
#     color='white',
#     fontstyle='italic', 
#     label='Design Download Popularity', 
#     loc='left'
# )
total_downloads = design_df['total downloads'].sum()
# Set the pie chart labels to white
for i, text in enumerate(labels):
    lbl = labels[i].get_text()
    val = float(autotext[i].get_text()[:-1])
    # if value less than 5% of sales, hide the
    # chart label & value for better visibility
    if val < 5:
        # print("-", lbl, val)
        labels[i].set_visible(False)
        autotext[i].set_visible(False)
    else: 
        labels[i].set_color('white')
        autotext[i].set_color('white')
        # text.set_color(patches[i].get_facecolor())

# set chart background transparent
design_pi.set_facecolor('none')
# display design popularity pie chart in the 2nd column
col2.pyplot(design_pi)