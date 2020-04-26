
# Summary

This project provides an analysis and evaluation of the impact of extreme weather on the time (The time between opening date and closing date of a complaint about **Sewer Back up** problem) to complete a 'Sewer Back up' problem in the City of Syracuse, New York.  The initial assumption is that the time to complete a sewer back up service request is delayed by extreme weather. In this Project, first I performed a data preparation process which include data cleaning, merging and  creating   new variables and dropping duplicates.  Second, after getting the final sample data ready, I tried to find the correlation between the completion time of request for sewer back up service (total_day) and extreme weather variables-if there is positive correlation between extreme weather's variables and completion time of addressing the sewer back up problem, means that the initial assumption is true  and extreme weather  delays the completion time of addressing sewer back up complaint. If the correlation is negative, means that the initial assumption is not true  and extreme weather in Syracuse doesn't delay the completion time of addressing sewer back up complaint. Finally, it should be
mentioned that creating extreme variable is based on my personal assumption because there is no any specific definition or criteria for extreme weather.

## Related questions

Which zip code recoded the highest number of request for fixing sewer back up problem?

Which zip code recoded the lowest request?

Totally, how many complaints  about sewer back up problem recorded during three years?

How many complaints recorded for each year?

What is the average time that DPW can address a complaint?

What is the correlation between extreme weather variables and the completion time of addressing sewer back up complaint ('total_days')? Does extreme  weather delay the completion time of fixing a sewer back up problem?


## Input data:

Two datasets have been used in this study: the first one is 'Cityline_Call_for_Services' (Published on October 29, 2019) that is publicly available in Syracuse Open Source data's website(http://data.syrgov.net/datasets/0aa5fcd76dbd4f2cabf2aeb1ddd0179e_0/data). the cityline dataset has 2021 rows and 22 columns.  The second dataset is weather dataset 'Daily_Weather_Syracuse_17to19.csv' which is available in NCEI website (https://www.ncdc.noaa.gov/cdo-web/search). The dataset contain 911 rows and 25 columns.  Both datasets contain data from 2017, 2018 and 2019.

### Deliverables:
Three deliverable files include one README.md file that explain the project step by step, one result.md file that briefly discuss on the findings and one python script  that is called 'final_project.py',  contains code used in this project.  The datasets used in this project also uploaded along  other deliverables.

#### Instruction:


1. Import the following modules: 're', 'pandas', 'numpy',  and 'from datetime import  datetime'.

2. Use pandas to read the  CSV file, 'Cityline_Calls_for_Service.csv', and store it into the variable 'dfc'.

3. To get information about columns and rows of dataset, use pandas.DataFrame.shape  and pandas.Dataframe.info().

4. To find the total number of complaint made for sewer back up problem, apply count() method to the 'complaint_type_name' column of cityline dataset.

5. Since the cityline dataset is a large dataset and contain different type
of complaints, we need to keep  the dataset just for 'Sewer Back up' complaint and drop all other rows except the rows that contain sewer back up complaint. To do so,  use  pandas DataFrame.loc and str.contains() methods as follows.  ('dfc.loc[dfc['complaint_type_name'].str.contains('Sew'), 'Sewer']=1' ) and drop all other rows that doesn't contains sewer back up complaint.

6. To find the number of sewer back up complaints per zip code, use groupby
mthod to 'zip' and 'complaint_type_name' columns as follows:
dfc2 = dfc.groupby('zip', as_index=False)['complaint_type_name'].count().copy()

7. To find which zip code has the highest number of complaints, use max()
 method to 'complaint_type_name' column of dfc2.

8. To find which zip code has the lowest number of complaints, use min() methods
 to 'complaint_type_name' columns of dfc2

9. Create the scatter plot of 'zip' and 'complaint_type_name' using dfc2 as Data
frame. To do so, set 'complaint_type_name' to y axis and 'zip' to x axis. The
scatter plot will show the zip code with highest number of complaints and the
zip code with lowest number of complaint as well.

10. To extract the time length  between open_date and close_date of complaints (the difference between open_date and close_date atributes of the dataset tell us how long does it take for Department ofPublic Work to fix the  'Sewer Back up' problem), the date's columns (open_date and close-date)  should be parsed based on Year/Month/Day by using regular expression for digit  character (|d). To do so,  we need to create new columns for each of them as follows:
'dfc['open_d2'] = dfc['open_date'].str.extract('(\d\d\d\d-\d\d-\d\d)', expand=True)'. Create 'close_d2' column for close_date using the same method.

11. Convert ['open_d2'] and ['close_d2'] columns into unified date format
by using pandas.to_datetime method. To do so,  set the 'open_d2' column of
dfc(cityline dataframe) to pandas.to_datetime method and 'open_d2' column of
dfc as its argument. Apply the same method to 'close_d2' column as well.


12. Create a new column, 'total_days', and set it to the difference  between 'close_d2' and 'open_d2' columns. Again, the 'total_days' column tell us how many days it takes Department of Public Work (DPW) to address the sewer back up problem.

13. Use pandas to read the  CSV file, 'Daily_Weather_Syracuse_17to19.csv', and store it into the variable 'dfw'. (It is the Syracuse Weather Dataset)

14. Now,  to merge both datasets based on date's columns we need to convert them into the same format . To do so, the only column that they can be merged is date's columns. Therefore, we need to convert both columns   into the same date format. As we did in step 5.


15. Rename both the 'DATE' column of weather dataset and 'close_d2' column of
 cityline dataset into a same name, df_merge. To do so, set the weather data
 frame to pandas.DataFrame.rename method as follow: 'dfw = dfw.rename(columns={"DATE": "df_merge"})'. Apply the same method to 'close_d2'  column of cityline dataset to rename it into df_merge as well.

16. do a left merge  and store the result of the merge into dfm.  To do so, set dfc as left dataset, dfw as right dataset and use df_merge as key to merge both
datasets, also set the 'validate' to 'm:1' and 'indicator' to 'True.

17. To find the average number of days that a 'sewer back up' complaint  is being addressed, apply the mean() method to 'total_days' comlum of merged dataset.

18. Now, from merged dataset (dfm), We create some indicator variables
that show extreme weather.  Suppose that if Average Daily Wind Speed('AWND')
is greater than 10 miles per hour, it is considered as extreme weather. Create
 new column called ['EX_wIND] and set to ['AWND'] column, greater than 10 and apply astype() method to it with argument 'int' that return the result as integer number.


 19. If snow dept ['SNWD'] is greater than 4 inches, it is extreme weather. Create new column called ['EX_SNWD'] and set it to ['SNWD'] column, also apply astype  method with 'int' argument to it.

 20. If maximum temperature ['TMAX'] is greater than 90, it is extreme weather. Create new column called ['EX_TMAX'] and set it to ['TMAX'] column, also apply astype  method with 'int' argument to it.

 21. If maximum temperature ['TMIN'] is smaller than 0, it is extreme weather. Create new column called ['EX_TMIN'] and set it to ['TMIN'] column, also apply astype method with 'int' argument to it.

 22. Create a new column called 'EX_SUM' which is the result of concatenation of
all extreme variables

23. To examine the correlation between extreme variables and 'total_days' column
which  is the lenght of time to address a complaint about sewer back up problem, create a subset of dfm (merged dataset) that just contain extreme variables and 'total-days'. Call the subset of dfm, dfm2.

24. Now, apply  pandas.DataFrame.corr method to dfm2 and print it.
