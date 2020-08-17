import pickle
import numpy as np
from tkinter import *

# with open('model.pkl','rb') as file:
#     model=pickle.load(file)
# vals=np.array([311,102,3,4,1]).reshape(1,-1)
# estimate=model.predict(vals)
# print(round(estimate[0][0],2))

def predict():
     vals1=int(entry1.get())
     vals2=int(entry2.get())
     vals3=float(entry3.get())
     vals4=int(entry4.get())
     vals5=int(entry5.get())
     with open('model.pkl','rb') as file:
         model=pickle.load(file)
     vals=np.array([vals1,vals2,vals3,vals4,vals5]).reshape(1,-1)
     estimate=model.predict(vals)
     pred=round(estimate[0][0]*100,2)
     #ol=Label(text=vals).grid(row=9,column=0)
     prediction=Label(text='Estimated chance of admission is : '+str(pred)).grid(row=7,column=0)

root=Tk()
title=Label(text='Admission prediction Score :',font=(20)).grid(row=0,column=0)
gre=Label(text='GRE Score').grid(row=2,column=0)
entry1=Entry(root,width=8)
entry1.grid(row=2,column=1)
toefl=Label(text='TOEFL Score').grid(row=3,column=0)
entry2=Entry(root,width=8)
entry2.grid(row=3,column=1)
cgpa=Label(text='CGPA').grid(row=4,column=0)
entry3=Entry(root,width=8)
entry3.grid(row=4,column=1)
rate=Label(text='University Rating').grid(row=5,column=0)
entry4=Entry(root,width=8)
entry4.grid(row=5,column=1)
research=Label(text='Research done').grid(row=6,column=0)
entry5=Entry(root,width=8)
entry5.grid(row=6,column=1)
calc=Button(text='Calculate',command=predict).grid(row=7,column=1)
mainloop()
