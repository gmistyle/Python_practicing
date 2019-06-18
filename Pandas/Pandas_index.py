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
