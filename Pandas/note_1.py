import pandas as pd

#function_1 : input file
names = ['col_1', 'col_2', 'col_3']
data_1 = pd.read_table('path or files names', sep = '|', header = None, names = user_cols)

#function_2 : input file
data_2 = pd.read_excel('path or files names', sheetname 'sheet_1')
