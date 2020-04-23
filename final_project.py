#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 00:05:14 2020

@author: alijanehsan
"""

#Step1.- Import the necessary library
import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd
import numpy as np
from datetime import datetime

pd.set_option('display.max_columns', 50)

#Step2.- Import Cityline Dataset

dfc = pd.read_csv('Cityline_Calls_for_Service.csv')
  

#step3. 
print(dfc.shape)
print(dfc.info())


#Step4
# To find the total number of complaint made for sewer back up problem, apply count() method
# to the 'complaint_type_name' atribute. 

print(dfc['complaint_type_name'].count())


#print(dfc['Sewer'].astype(int).value_counts())

#step 5 to keep dataset just for sewer back up complaint

dfc.loc[dfc['complaint_type_name'].str.contains('Sew'), 'Sewer']=1
dfc.loc[dfc['Sewer'] != 1, 'Sewer'] = 0
droprows = dfc[dfc['Sewer'] == 0].index
dfc.drop(droprows, inplace = True)

#step 6 To find the number of sewer back up complaints per zip code,

dfc2 = dfc.groupby('zip', as_index=False)['complaint_type_name'].count().copy()

#step 7. To find which zip code has the highest number of complaints

print(dfc2['complaint_type_name'].max())
 
# the zip code 13205 has the highest number of complaint which is 3342

#step 8. To find which zip code has the lowest number of sewer back up complaint

print(dfc2['complaint_type_name'].min())

# The zip code 13215 has lowest number of complaint which is 13

#step 9
# Create the scatter plot of 'zip' and 'complaint_type_name' using dfc2 as Data
#fram

ax1 = dfc2.plot.scatter(x='zip',
                      y='complaint_type_name',
                      c='green')

#Step 10

dfc['open_d2'] = dfc['open_date'].str.extract('(\d\d\d\d-\d\d-\d\d)', expand=True)
dfc['close_d2'] = dfc['close_date'].str.extract('(\d\d\d\d-\d\d-\d\d)', expand=True)

#step 11
 
dfc['open_d2'] = pd.to_datetime(dfc['open_d2'])
dfc['close_d2'] = pd.to_datetime(dfc['close_d2'])

#step 12
dfc['total_days'] = dfc['close_d2'] -dfc['open_d2']



#step 13

dfw = pd.read_csv('Daily_Weather_Syracuse_17to19.csv')


#step 14. convert the merging key into same date format. 
dfw['DATE']=  pd.to_datetime(dfw['DATE'])
dfc['close_d2'] = pd.to_datetime(dfc['close_d2'])
#Rename the 'DATE' columns



#Step 15. Rename the merging keys.
 
dfw = dfw.rename(columns={"DATE": "df_merge"})
dfc = dfc.rename(columns={'close_d2': "df_merge"})





#step 16

dfm = pd.merge(dfc,
                dfw, 
                on = 'df_merge', 
                how = 'left', 
                validate = "m:1", 
                indicator = True 
               )


# Step 17. To find the average number of days that a 'sewer back up' complaint  is being addressed

print(dfm['total_days'].mean())

#step 18. Create variables to define extreme weather

dfm['EX_WIND'] = (dfm['AWND'] > 10).astype(int)

# step 19 

dfm['EX_SNWD'] = (dfm['SNWD'] > 4).astype(int)
 
#step 20
 
dfm['EX_TMAX'] = (dfm['TMAX'] > 90).astype(int)

#step 21

dfm['EX_TMIN'] = (dfm['TMIN'] < 0).astype(int)

#step 22
dfm['EX_SUM'] = dfm['EX_WIND'] + dfm['EX_SNWD'] +dfm['EX_TMAX'] + dfm['EX_TMIN']

#step 23

dfm2 = dfm[['total_days', 'EX_SUM', 'EX_WIND',  'EX_SNWD', 'EX_TMAX', 'EX_TMIN']]

#step 24
print(dfm2.corr())


#
#To find the number of sewer back up complaints for each year:


#dfm.loc[dfm['open_date'].str.contains('2017'), 'year'] = 2017
#dfm.loc[dfm['open_date'].str.contains('2018'), 'year'] = 2018
#dfm.loc[dfm['open_date'].str.contains('2019'), 'year'] = 2019
#dfm['year'] = dfm['year'].astype(int)
#print(dfm['year'].astype(int).value_counts())

# To find the average time that it takes  DPW to address a complaint:
#print(dfm['total_days'].mean())

#print(dfc.loc[dfc['complaint_type_name' ].str.contains('Sewer Back Up')].count())

#print(dfm['complaint_type_name'].count())
#dfm = dfm['zip'].fillna(0)
#dfc2 = dfc.groupby('zip', as_index=False)['complaint_type_name'].count().copy()
#dfc2.sort_values('complaint_type_name', ascending = True)
#print(dfc2)

