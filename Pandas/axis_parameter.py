import pandas as pd

data.drop('col_name', axis = 1)
#drop the column called 'col_name'

data.drop(2, axis = 0)
#drop the row that index = 2

'''
axis = 1 tells that the direction of every operation is a horizantal movement
axis = 0 tells that the direction of every operation is vertical
'''

data.mean(axis = 0) #calculate means by columns, axis is default to zero
data.mean(axis = 1) #claculate means by rows, which is a meaningless number due to the unit between every columns should be different
