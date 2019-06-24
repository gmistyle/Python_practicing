#import pandas as pd
ufo = pd.read_csv('http://bit.uforeports')
ufo.shape()
ufo.head()

ufo.drop('City', axis = 1).head() #not effect underlying data
ufo.drop('City', axis - 1, inplace = True) #underlying data set is effected

#it not guarantee
ufo.set_index('Time', inplace = True) #it won't create second copy of data but only make the change inplacely 
ufo = ufo.set_index('Time') #this way could be much slower when the scale of data is huge because it will create a second copy of data

#use the advantage of "inplace = False" when you are not sure about some method and intend to try it
