import pickle
import numpy as np
from tkinter import *

# with open('model.pkl','rb') as file:
#     model=pickle.load(file)
# vals=np.array([311,112,3,9,0]).reshape(1,-1)
# estimate=model.predict(vals)
# print(estimate)

def predict():
     flag=0
     global err
     vals1=int(entry1.get())
     if vals1 not in range(1,341):
        err=Label(root,text='Please enter a valid score',fg='red').grid(row=2,column=2)
        flag=1
     vals2=int(entry2.get())
     if vals2 not in range(1,121):
        err=Label(root,text='Please enter a valid score',fg='red').grid(row=3,column=2)
        flag=1
     vals3=int(entry3.get())
     if vals3 not in range(1,6):
        err=Label(root,text='Please enter a valid rating',fg='red').grid(row=4,column=2)
        flag=1
     vals4=float(entry4.get())
     if vals4<0 or vals4>10:
        flag=1
        err=Label(root,text='Please enter a valid score',fg='red').grid(row=5,column=2)
     vals5=vl.get()
     if flag==0:
        with open('model.pkl','rb') as file:
            model=pickle.load(file)
        vals=np.array([vals1,vals2,vals3,vals4,vals5]).reshape(1,-1)
        estimate=model.predict(vals)
        pred=round(estimate[0][0]*100,2)
        if pred<0:
            prediction=Label(text='Chances of admission is less than 10%').grid(row=10,column=0)    
        else:
            prediction=Label(text='Estimated chance of admission is : '+str(pred)+'%').grid(row=10,column=0)

def clearall():
    entry1.delete(0)
    entry2.delete(0)
    entry3.delete(0)
    entry4.delete(0)  


root=Tk()
root.geometry('400x400')
vl=IntVar()
root.title('Admission prediction')
title=Label(text='Admission prediction Score :',font=(20)).grid(row=0,column=0)
gre=Label(text='GRE Score').grid(row=2,column=0)
entry1=Entry(root,width=8)
entry1.grid(row=2,column=1)
toefl=Label(text='TOEFL Score').grid(row=3,column=0)
entry2=Entry(root,width=8)
entry2.grid(row=3,column=1)
rate=Label(text='University Rating').grid(row=4,column=0)
entry3=Entry(root,width=8)
entry3.grid(row=4,column=1)
cgpa=Label(text='CGPA').grid(row=5,column=0)
entry4=Entry(root,width=8)
entry4.grid(row=5,column=1)
research=Label(text='Research done').grid(row=6,column=0)
R1=Radiobutton(text='Yes',value=1,variable=vl).grid(row=6,column=1)
R1=Radiobutton(text='No',value=0,variable=vl).grid(row=7,column=1)
calc=Button(text='Calculate',command=predict).grid(row=9,column=0)
clear=Button(text='Clear',command=clearall,width=8).grid(row=9,column=1)
mainloop()
