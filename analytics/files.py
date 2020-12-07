import pandas as pd

def read_data(file,ftype='csv'):
    if ftype=='csv':
        dataset=pd.read_csv(file)
    elif ftype=='json':
        dataset=pd.read_json(file)
    return dataset