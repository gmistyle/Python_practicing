import pandas as pd

#check if there is a missing value
data.isnull().tail()
data.notnull

#summation of the total missing value
data.isnull().sum(axis = 0) #axis default to zero

#show the rows that is missing in a specific column
data[data.col_name.isnull()]

#drop missing value
#how = 'any' : drop the row if any value in the row is missing
data.dropna(how = 'any')
data.dropna(how = 'any').shape

#how = 'all' : drop the row if all of the value in the row are missing
data.dropna(how = 'all')

#drop the row if the specific columns have missing value
data.dropna(subset = ['col_1', 'col_2'], how = 'any')

#show the number of missing value while using value_counts method
data['col_name'].value_counts(dropna = False)

#fill in the missing value with a new value
data['col_name'].fillna(value = 'new_value', inplace = True)
