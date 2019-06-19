import pandas as pd

#show the length and index of a series
data.index()

#output the value of a specific row in a specific column
data.loc[23, 'col_name'] #23 is the index of the specific row

#reset the index by the values of a column
data.set_index('col_name', inplace = True)
data.index.name = None #delete the first row that represents as index name

#cancel the change in the previous step
data.index.name = 'col_name'
data.reset_index(inplace = True)
data.head()

#usage_1
data.set_index('col_name', inplace = True)
data.head()
data.col_name.head()
data.col_name.value_counts()
data.col_name.value_counts().values #show the value of method "value_count"
data.col_name.value_counts()['index_name'] #it will output the value counts of that index name

#sorting by index
data.col_name.value_counts().sort_index()

#alignment
People = pd.Series([3000000, 85000], index = ['Taiwan', 'Japan'], name = 'Population')
Beer_serving = pd.Series([10000, 20000], index = ['Taiwan', 'Japan'], name = 'Beer_serving')
New_Series = People*Beer_serving #it will multiple two series by the index name, ex: the population of Taiwan*the beer serving of Taiwan

#append new_series to old dataframe
pd.concat([old_data, new_series], axis = 1) #the index should be the same
              

 
                 
