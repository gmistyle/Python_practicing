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
data.dtypes                     
###select series
data.col_1 #it could conflict with some built_in function
data['col_1'] #it would be more
                     
###create new series
data['new_col'] = data['col_1'] + ',' + data['col_2']
