import pandas as pd
import csv
import matplotlib.pyplot as plt
df = pd.read_csv("googleplaystore.csv", delimiter =",")



# Question-1 Display the first 20 rows and first 3 columns. 
print("\n\nQuestion-1 Display the first 20 rows and first 3 columns.")
print(df.iloc[0:20,0:3])



# Question-2 Count total number of rows.
print("\n\nQuestion-2 Count total number of rows.")
index = df.index
number_of_rows = len(index)
print(number_of_rows)



# Question-3 Display records where the column 'App' contains the word "photo".
print("\n\nQuestion-3 Display records where the column 'App' contains the word 'photo'.")
filt = df['App'].str.contains('photo', na=False)
print(df.loc[filt, 'App'])



# Question-4 Display the Apps with value of rating greater than 2 but less than 3.
print("\n\nQuestion-4 Display the Apps with value of rating greater than 2 but less than 3.")
comparision = (df['Rating'] < 3) & (df['Rating'] > 2)
print(df['App'][comparision]) 



# Question-5 Calculate the median for ‘Rating’ attribute.
print("Question-5 Calculate the median for ‘Rating’ attribute.")
print(df['Rating'].median(skipna = True))



# Question-6 Find the minimum, maximum and average value for ‘Rating’.
print("\n\nQuestion-6 Find the minimum, maximum and average value for ‘Rating’.")
print("\n")
# minimum
print("Minimum")
print(df['Rating'].min())
print("\n")
print("Maximum")
# maximum
print(df['Rating'].max()) 
print("\n")
print("Average")
# average
print(df['Rating'].mean())  



# Question-7 Display the Apps that belongs to "Family" or "Medical" category and rating greater than 3.
print("\n\nQuestion-7 Display the Apps that belongs to 'Family' or 'Medical' category and rating greater than 3.")
print("\n")
print("First 40 rows:")
print("\n")
first_query = ((df['Category'] == 'FAMILY') | (df['Category'] == 'MEDICAL'))
second_query = first_query & (df['Rating'] > 3)
new = df.loc[second_query, ['App', 'Rating']]
pd.set_option('display.max_rows', None)
print(new.head(40))



# Question-8 Sort the records as per the descending order of ‘Category’ and 'Rating'.
print("\n\nQuestion-8 Sort the records as per the descending order of ‘Category’ and 'Rating'.")
print("\n")
print("First 40 rows:")
print("\n")
for_rating = df.sort_values(by=['Rating', 'Category'], ascending = False, na_position='last')
pd.set_option('display.max_rows', 10)
print(for_rating[['App', 'Rating', 'Category']].head(40))



# Question-9 Rename column name ‘Type’ with ‘App Type’.
print("\n\nQuestion-9 Rename column name ‘Type’ with ‘App Type’.")
print("Before")
print(df.columns)
df.rename(columns={'Type':'App Type'}, inplace=True)
print("After")
print(df.columns)



# Question-10 Generate a horizontal bar chart of Type Vs. Average Rating.
# numm = df['Rating'].mean()
# def convert_str_to_int(x):
#     if x == 'Free':
#         return 0
#     if x == 'Paid':
#         return 1
    
# df['Converted_Type'] = df['Type'].apply(convert_str_to_int)
# print(df[['Type','Converted_Type']].head())
# plt.bar(df['Converted_Type'], numm)
# plt.show()
# first_query = (df['Type'] == 'Paid')
# new = df.loc[first_query, ['App', 'Rating', 'Type']]
# print(new)