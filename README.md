User Manual To Run The Code 
1. Introduction 
Ukulele Tuesday Data Analysis – This program is targeted to Ukulele Tuesday group to allow analysis 
on its collection of songs. The application allows for querying and filtering song data and view trends 
in performances. 
2. Installation and Setup 
1. Download and install Python from python.org. 
2. Install the required libraries – PyQT6, Pandas, Matplotlib 
3. Download the program files in a location of your choice. 
4. Locate your data files (in csv format) – Tabdb.csv, Playdb.csv, Requestdb.csv (your files can have 
any name) 
3. Program flow 
3.1 Loading Data Files 
1. Open the program. 
2. Upload files tabdb.csv, playdb.csv, and requestdb.csv. 
3. The program will validate your data (as per section 5) for consistency, reporting (an error 
message window will pop up) any missing columns or errors in data format. You must correct 
your data in the files and re-upload to move forward. 
4. Confirm successful data loading by reviewing the summary displayed. 
5. Click on ‘NEXT’ button to go to Query Page. 
3.2 Filtering and Querying Data 
1. Navigate through the tabs to query data for each file. 
2. Select the columns to display (e.g., title, artist, duration) and enter date range to narrow down 
the results. 
3. Click ‘APPLY FILTERS’ to display the filtered results in a table/pie-chart. 
4. Click on ‘NEXT’ button to see the graphs. 
3.3 Generating Plots 
1. Navigate through the tabs to see the plots. 
2. The section contains 7 tabs with graphical data (based on entire data given by user) with each 
type of graph mentioned below. 
The program offers the following visualizations: 
a. 
Histogram of Songs by Difficulty: Visualizes the distribution of song difficulty 
levels. 
b. Histogram of Songs by Duration: Provides a view of song lengths. 
c. 
Bar Chart of Songs by Language: Shows language distribution. 
d. Bar Chart of Songs by Source: Compares songs from different sources. 
e. 
Bar Chart of Songs by Decade: Groups songs based on their release decade. 
f. 
Cumulative Line Chart of Songs Played Over Time: Shows the trend of song 
performances. 
g. Pie Chart of Songs by Gender: Visualizes the gender of lead vocalists in a pie chart 
format. 
3. Click on ‘DOWNLOAD ALL GRAPHS (PDF)’ to get a local copy of all plots. 
