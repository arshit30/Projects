import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle
from sklearn.linear_model import LinearRegression

data=pd.read_csv('C:/Users/ARSHTVIK/Documents/Machine learning/DATASETS/Classification/Admission_predict.csv')
data.drop(columns=['Serial No.'],axis=0,inplace=True)
X=data[['GRE Score','TOEFL Score','University Rating','CGPA','Research']]
Y=data[['Chance of Admit ']]
train_x,test_x,train_y,test_y=train_test_split(X,Y,test_size=0.1)
lrt=LinearRegression()
lrt.fit(train_x,train_y)
print(lrt.score(train_x,train_y))
print(lrt.score(test_x,test_y))


val=np.array([321,112,3,9,1])
print(lrt.predict(val.reshape(1,-1)))

with open('model.pkl','wb') as w:
    pickle.dump(lrt,w)