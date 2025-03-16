# AnimeShowsDataCleaning
* GWC Python Project for Club Workshop
* Anime Data Cleaning Project

# **Description**
This Python script cleans data from a CSV file containing information about anime shows. It removes missing values, duplicates, and incomplete entries (anime with fewer than 5 episodes), preparing the data for further analysis.

# **Requirements**
* Python 3.x
* pandas library (install with pip install pandas)

# **Steps Performed**
* Import pandas: We use pandas to handle the data.
* Load Data: Reads the CSV file into a DataFrame (df).
* Show Unclean Data: Prints the raw data to the console.
* Check Columns: Lists the columns to ensure correct data.
* Handle Missing Data: Removes rows with missing episode numbers.
* Remove Duplicates: Removes duplicate anime names.
* Filter Incomplete Shows: Removes anime with fewer than 5 episodes.
* Show Cleaned Data: Prints the final cleaned data.

# **How to Use**
* Prepare Your CSV File: Ensure your file has column titles.
* Update File Path: Modify this line in the script to point to your file:
* python
* Copy code
* df = pd.read_csv('/path/to/your/animedata.csv')
* Run the Script: Execute the script to clean your data.
* Further Analysis: Use the cleaned DataFrame for analysis or export it.
