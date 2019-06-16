import pandas as pd

###input files
#function_1
names = ['col_1', 'col_2', 'col_3']
data_1 = pd.read_table('path or file name', sep = '|', header = None, names = user_cols)

#function_2
#the only different is the 'sep'
data_2 = pd.read_excel('path or file name', sheetname 'sheet_1')
data_3 = pd.read_csv('path or file name)
                   
#show some datas
data.head()
#descriptive statistics
data.describe(include = ['data_type : {float64, object,}'])                     
#function       
data.shape
data.dtypes #(nums of rows, nums of cols)                     
###select series
data.col_1 #it could conflict with some built_in function
data['col_1'] #it would be more
                     
###create new series
data['new_col'] = data['col_1'] + ',' + data['col_2']
                     
#rename couloums in DataFrame
data.coloumns #attribute that shows cols_name                     
#method_1                     
data.rename(columns = {'old_name_1' : 'new_name_1', 'old_name_2 : new_name_2'}, inplace = True)                     
#method_2
data_cols_name = ['col_1', 'col_2', 'col_3']
data.columns = data_cols_name   
#method_3
#modify cols name during reading the file
data = pd.read_csv('path', names = data_cols_name, header = 0) #header = 0 tells that the dataframe doesnt need a new header                     
#method_4
data.columns = data.columns.str.replace(' ', '_') #replace space with underscore   

#drop a column from a dataframe
#axis 1 equals col, axis 0 equals row(default)                     
data.drop('col_Name', axis = 1, inplace = True) #one at a time
data.drop(['col_1', 'col_2'], axis = 1, inplace = True) #multiple at a time
                     
#drop a row from a dataframe
data.drop([0, 1, 3], axis = 0, inplace = True)                   
