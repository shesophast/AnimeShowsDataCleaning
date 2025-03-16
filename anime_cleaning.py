import pandas as pd

#Reading Data from CSV
df =pd.read_csv('/Users/shesophast/GWC Projects/AnimeShowsDataCleaning/animeproject/animedata.csv')

print ("Unclean Data")
print(df)

#Read all columns and check their names to avoid errors
df =pd.DataFrame(df)
df.head()
column_list = list(df.columns)
print(column_list)

#Checking for any null values (lack of value in a column)
nullValues = df.isna().sum()
print(nullValues)
#Deleting Null Data
df= df.dropna(subset=['Episodes'])
print(df)

#Checking for Duplicates
animeName=df.duplicated('Anime Name')
print(animeName)
#Deleting Duplicates
df = df.drop_duplicates('Anime Name')
print(df)

#Checking to see if Episode are less than 5
incompleteSeries= df[df['Episodes'] < 5].sum()
print(incompleteSeries)
#Deleting incomplete series
df = df[df['Episodes'] >= 5]
print(df)

#Printing Clean Data
print("Clean Data")
print(df)

