import pandas as pd

#sort a pandas dataframe or series
#series method
data.col_name.sort_values(ascending = False) #default = True
#dataframe method
data.sort_values('col_name')
#sort two cols at a time
data.sort_values(['col_name_1', 'col_name_2'])

#filter rows of a pandas dataframe by columns value
#method_1
new_pd_series = data.col >= 200
data[new_pd_series] #the filter step
#method_2
data[data.col >= 200] #output a dataframe
data[data.col >= 200].col_1 #output a pd series
data[data.col >= 200]['col_1'] #output a pd series
data.loc[data.col >= 200, 'col_1'] #output a pd series
data[(data.col_1 >= 200) & (data.col_2 >= 300)] #cant use and/or but only &/|

#filter by multiple condition in one columns
data.col.isin(['first', 'second', 'third'])

#use string methods in pandas
data.col_name.str.method_name()

#change the data type of a pandas series
data['col_name'] = data.col_name.astype(float)
#change the data type of a pandas series while reading the data
data = pd.read_csv('path', dtype = {'col_name' : float})

#groupby method
data.groupby('col_name').col_name_2.mean()
#multiple function when using groupby method
data.groupby('col_name').col_name_2.agg(['count', 'min', 'max', 'mean'])

#basic process of exploring a pandas series
data.dtypes #show the data types of every column
data.col_name.describe() #descriptive statistics of the column
data.col_name.value_counts() #calculate the frequence of every unique value
data.col_name.value_counts(normalize=True) #calculate the percentage of the frequence of every unique value
data.col_name.unique() #shows the number of every unique value of the column
data.col_name.nunique() #shows every unique value of the column
#
pd.crosstab(data.col_1, data.col_2) #show the cross table of these two columns
