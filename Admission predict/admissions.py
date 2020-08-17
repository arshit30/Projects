import pickle
import numpy as np
with open('model.pkl','rb') as file:
    model=pickle.load(file)

val=np.array([328,106,3,8.98,1]).reshape(1,-1)
print(model.predict(val))
