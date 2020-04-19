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

4. To extract the time length  between open_date and close_date of complaints (the difference between open_date and close_date atributes of the dataset tell us how long does it take for Department ofPublic Work to fix the  'Sewer Back up' problem), the date's columns (open_date and close-date)  should be parsed based on Year/Month/Day by using regular expression for digit  character (|d). To do so,  we need to create new columns for each of them as the following:
'dfc['open_d2'] = dfc['open_date'].str.extract('(\d\d\d\d-\d\d-\d\d)', expand=True)' create 'close_d2' column for close_date using the same method.

5. Convert ['open_d2'] and ['close_d2'] columns into unified date format
by using pandas.to_datetime method. To do so,  set the 'open_d2' column of
dfc(cityline dataframe) to pandas.to_datetime method and 'open_d2' column of
dfc as its argument. Apply the same method to 'close_d2' column as well.

6. Create a new column, 'total_days', and set it to the difference  between 'close_d2' and 'open_d2' columns. Again, the 'total_days' column tell us how many days it takes Department of Public Work (DPW) to address the sewer back up problem.

7. Use pandas to read the  CSV file, 'Daily_Weather_Syracuse_17to19.csv', and store it into the variable 'dfw'.
