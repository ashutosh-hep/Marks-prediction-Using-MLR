
import tkinter.messagebox
import pandas as pd  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import tkinter as t
import numpy as np
import csv

class MyWindow:
    def __init__(self, win):
        self.lbl1=t.Label(window, text="Student Subject Prediction System", fg='red', font=("Helvetica", 20))
        self.lbl1.place(x=200, y=10)    
      #  self.lbl5=t.Label(window, text="Or", fg='blue', font=("Helvetica", 15))
       # self.lbl5.place(x=415, y=(310+107))
        self.lbl2=t.Label(win, text='Enter the Roll Number:', fg='blue',font=("Helvetica", 10))
        self.lbl2.place(x=250, y=65)
        self.t1=t.Entry(bd=2)
        self.t1.place(x=390, y=65)        
        self.b1=t.Button(win, text='Enter', command=self.displayStud)
      #  self.b6=t.Button(window,text='Predict Class Average Result',command=self.Message4)
       # self.b6.place(x=358, y=(310+151.5))
        self.b1.place(x=540, y=60)
        
    def readcsv(self,file):
        ifile = open(file, "r")
        reader = csv.reader(ifile)
        rownum = 0
        a = []
        for row in reader:
            temp=[float(i) for i in row]
            a.append (temp)
            rownum += 1
        ifile.close()
        return a
    
    def Coefficient(self,XMat,YMat):
        XT = [[XMat[j][i] for j in range(len(XMat))] for i in range(len(XMat[0]))]
        XTX=[[sum(a*b for a,b in zip(XT_row,XMat_col)) for XMat_col in zip(*XMat)] for XT_row in XT]
        InMat = np.linalg.inv(XTX)
        TempMat=[[sum(a*b for a,b in zip(InMat_row,XT_col)) for XT_col in zip(*XT)] for InMat_row in InMat]
        resultMat=[[sum(a*b for a,b in zip(TempMat_row,YMat_col)) for YMat_col in zip(*YMat)] for TempMat_row in TempMat]
        return resultMat
    
    def displayStud(self):        
        with open('Stud.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            fields = next(csvreader)
            p=300
            q=120
            for i in range(len(fields)):
                self.lbl1=t.Label(window, text=fields[i]+":", fg='black', font=("Helvetica", 13))
                self.lbl1.place(x=p, y=q)
                q=q+30
            a=390
            b=120
            
            for row in csvreader:
                if str(row[0])==str(self.t1.get()):
                    for j in range(len(row)):
                        self.lbl2=t.Label(window, text=row[j], fg='green', font=("Helvetica", 13))
                        self.lbl2.place(x=a, y=b)
                        b=b+30 
                    self.b2=t.Button(window,text='Predict Result',command=self.Message1)
                    self.b2.place(x=555, y=180) 
                    self.b10=t.Button(window,text='Predict Class AVG Result',command=self.Message1)
                    self.b10.place(x=650, y=180)
                    
                    self.b3=t.Button(window,text='Predict Result',command=self.Message2)
                    self.b3.place(x=555, y=210) 
                    self.b11=t.Button(window,text='Predict Class AVG Result',command=self.Message2)
                    self.b11.place(x=650, y=210)
                    
                    self.b4=t.Button(window,text='Predict Result',command=self.Message3)
                    self.b4.place(x=555, y=240) 
                    self.b12=t.Button(window,text='Predict Class AVG Result',command=self.Message3)
                    self.b12.place(x=650, y=240)
                    
                    self.b5=t.Button(window,text='Predict Result')
                    self.b5.place(x=555, y=270)
                    
                    self.b5=t.Button(window,text='Predict Result',command=self.Message5)
                    self.b5.place(x=555, y=300)
                    self.b13=t.Button(window,text='Predict Class AVG Result',command=self.Message5)
                    self.b13.place(x=650, y=300)
                    
                    self.b5=t.Button(window,text='Predict Result',command=self.Message6)
                    self.b5.place(x=555, y=330)
                    self.b14=t.Button(window,text='Predict Class AVG Result',command=self.Message6)
                    self.b14.place(x=650, y=330)
                    
                    self.b5=t.Button(window,text='Predict Result',command=self.Message7)
                    self.b5.place(x=555, y=360)
                    self.b15=t.Button(window,text='Predict Class AVG Result',command=self.Message7)
                    self.b15.place(x=650, y=360)
                    
                    self.lbl5=t.Label(window, text="Subject5:", fg='black', font=("Helvetica", 13))
                    self.lbl5.place(x=300, y=(300))
                    self.lbl6=t.Label(window, text="Artificial Intelligence", fg='green', font=("Helvetica", 13))
                    self.lbl6.place(x=390, y=(300))
                    self.lbl7=t.Label(window, text="Subject6:", fg='black', font=("Helvetica", 13))
                    self.lbl7.place(x=300, y=(330))
                    self.lbl8=t.Label(window, text="Soft project Mang.", fg='green', font=("Helvetica", 13))
                    self.lbl8.place(x=390, y=(330))
                    self.lbl9=t.Label(window, text="Subject7:", fg='black', font=("Helvetica", 13))
                    self.lbl9.place(x=300, y=(360))
                    self.lbl10=t.Label(window, text="Sofware Engg.", fg='green', font=("Helvetica", 13))
                    self.lbl10.place(x=390, y=(360))
                    
                    

                    break
                else:
                    self.lbl2=t.Label(window, text="Wrong Input", fg='green', font=("Helvetica", 13))
                    self.lbl2.place(x=a, y=b)
                
                   
    def Message1(self):
        XMat=self.readcsv('MLInput.csv')
        YMat=self.readcsv('MLOutput.csv')
        CoeMat=self.Coefficient(XMat,YMat)
        Sub=["Maths2","Statistics","DAA","Logical Ability(10:100)","Mid1","Mid2"]
        B0=CoeMat[0]
        T1=B0[0]
        Y=float(T1)
        j=0
        for i in range(1,7):
            B=CoeMat[i]
            T=B[0]
            X=float(input("Enter "+Sub[j]+" Marks:"))
            Y=Y+float(T)*X
            j=j+1
        res=str(int(Y))
        t.messagebox.showinfo(title="Predicted marks:", message=(res))
        

        
              
    def Message2(self):
        XMat=self.readcsv('SignalInput .csv')
        YMat=self.readcsv('SignalOutput .csv')
        CoeMat=self.Coefficient(XMat,YMat)
        Sub=["Signals & Systems","Information & Security","Networking","Logical Ability(10:100)","Mid1","Mid2"]
        B0=CoeMat[0]
        T1=B0[0]
        Y=float(T1)
        j=0
        for i in range(1,7):
            B=CoeMat[i]
            T=B[0]
            X=float(input("Enter "+Sub[j]+" Marks:"))
            Y=Y+float(T)*X
            j=j+1
        res=str(int(Y))
        t.messagebox.showinfo(title="Predicted marks:", message=res)
        
    def Message3(self):
        XMat=self.readcsv('BigDataInput.csv')
        YMat=self.readcsv('BigDataOutput.csv')
        CoeMat=self.Coefficient(XMat,YMat)
        Sub=["DBMS","Data Mining","OAS","Logical Ability[10:100]","Mid1","Mid2"]
        B0=CoeMat[0]
        T1=B0[0]
        Y=float(T1)
        j=0
        for i in range(1,7):
            B=CoeMat[i]
            T=B[0]
            X=float(input("Enter "+Sub[j]+" Marks:"))
            Y=Y+float(T)*X
            j=j+1
        res=str(int(Y))
        t.messagebox.showinfo(title="Predicted marks:", message= res)
        

    def Message5(self):
        XMat=self.readcsv('AI input.csv')
        YMat=self.readcsv('AIOutput.csv')
        CoeMat=self.Coefficient(XMat,YMat)
        Sub=["AI","SCT","Neurak Networks","Logical Ability(10:100)","Mid1","Mid2"]
        B0=CoeMat[0]
        T1=B0[0]
        Y=float(T1)
        j=0
        for i in range(1,7):
            B=CoeMat[i]
            T=B[0]
            X=float(input("Enter "+Sub[j]+" Marks:"))
            Y=Y+float(T)*X
            j=j+1
        res=str(int(Y))
        t.messagebox.showinfo(title="Predicted marks:", message=res)
        
              
    def Message6(self):
        XMat=self.readcsv('SPMInput.csv')
        YMat=self.readcsv('SPMOutput.csv')
        CoeMat=self.Coefficient(XMat,YMat)
        Sub=["Process","PPL","Data communication","Logical Ability(10:100)","Mid1","Mid2"]
        B0=CoeMat[0]
        T1=B0[0]
        Y=float(T1)
        j=0
        for i in range(1,7):
            B=CoeMat[i]
            T=B[0]
            X=float(input("Enter "+Sub[j]+" Marks:"))
            Y=Y+float(T)*X
            j=j+1
        res=str(int(Y))
        t.messagebox.showinfo(title="Predicted marks:", message=res)
        
        
              
    def Message7(self):
        XMat=self.readcsv('SEInput.csv')
        YMat=self.readcsv('SEOutput.csv')
        CoeMat=self.Coefficient(XMat,YMat)
        Sub=["SE","software Testing","ECM","Logical Ability(10:100)","Mid1","Mid2"]
        B0=CoeMat[0]
        T1=B0[0]
        Y=float(T1)
        j=0
        for i in range(1,7):
            B=CoeMat[i]
            T=B[0]
            X=float(input("Enter "+Sub[j]+" Marks:"))
            Y=Y+float(T)*X
            j=j+1
        res=str(int(Y))
        t.messagebox.showinfo(title="Predicted marks:", message=res)
        
        

window=t.Tk()
mywin=MyWindow(window)
window.title('Stanley Engg. College')
window.geometry("800x650+10+10")

window.mainloop()



dataset = pd.read_csv('StudDataNew.csv')
X = dataset[['MAT2', 'DMAT', 'SNME', 'DS', 'DAA', 'DBMS', 'AI', 'DWDM', 'LOGIC', 'MID1','MID2']].values
y = dataset['ML'].values
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.4)
clf = LinearRegression()
clf.fit(X_train, y_train)
clf.score(X_test, y_test)
t.messagebox.showinfo(title="Accuracy of the model is:", message=((clf.score(X_test, y_test)*100),"%"))

window.mainloop()

