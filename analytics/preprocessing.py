import pandas as pd
from sklearn.preprocessing import *

def remove_nan(data,cols='None'):
    if cols=='None':
        return data.dropna()
    else:
        if type(cols)==list:
            return data.dropna(subset=cols)
        else:
            return data.dropna(subset=[cols])
            
def categorical(data,cols=None,dtype='categorical'):
    if dtype=='categorical':
        encoder=LabelEncoder()
        data[cols]=encoder.fit_transform(data[cols])
        return data