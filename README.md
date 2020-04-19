# Final_Project
Advanced Policy Analysis -Final Project
# Summary

This project provides an analysis and evaluation of the impact of extreme weather on the time (The time between opening date and closing date of a complaint about **Sewer Back up** problem) to complete a 'Sewer Back up' problem in the City of Syracuse, New York.  The initial assumption is that the time to complete a sewer back up service request is delayed by extreme weather. In this Project, first I performed a data preparation process which include data cleaning, merging and  creating   new variables and dropping duplicates.  Second, after getting our final sample data ready, I tried to find the correlation between the completion time of request for sewer back up service (total_day) and extreme weather variables-if there is positive correlation between extreme weather's variables and completion time of addressing the sewer back up problem, means that the initial assumption is true  and extreme weather  delays the completion time of addressing sewer back up complaint. If the correlation is negative, means that the initial assumption is not true  and extreme weather in Syracuse doesn't delay the completion time of addressing sewer back up complaint.

#Input data

Two datasets have been used in this project: the first one is 'Cityline_Call_for_Services' (Published on October 29, 2019) that is publicly available in Syracuse Open Source data's website(http://data.syrgov.net/datasets/0aa5fcd76dbd4f2cabf2aeb1ddd0179e_0/data), and the second dataset is weather dataset 'Daily_Weather_Syracuse_17to19.csv' which is available in NCEI website (https://www.ncdc.noaa.gov/cdo-web/search).

# Instruction:


1. Import the following modules: 're', 'pandas', 'numpy', 'from datetime import  datetime'.

2. Use pandas to read the  CSV file, 'Cityline_Calls_for_Service.csv', and store it into the variable 'dfc'.

3. Since the cityline dataset is a large dataset and contain different type
of complaints, we need to keep  the dataset just for 'Sewer Back up' complaint and drop all other rows except the rows that contain sewer back up complaint. To do so, from the  'complaint_type_name' field,  use  pandas DataFrame.loc and str.contains() methods ('dfc.loc[dfc['complaint_type_name'].str.contains('Sew'), 'Sewer']=1' ) and drop all other rows that doesn't contains sewer back up complaint.
