#GUI VERSION 1.1
# A SIMPLE INTERST CALCULATOR
#with single button to calculate
from Tkinter import * #IMPORT EVERYTHING FOR GUI CREATION 
    
def Calculate():                               # FUNCTION FOR CALCULATING INTERST AND AMOUNT
    mtext1=float(ment.get()*ment2.get()*ment3.get())/100  #CALCULATE INTERST
    mlabel1=Label(mgui,text=mtext1).place(x=140,y=200)
    mtext2=float(ment.get()+mtext1)                     # CALCULATE AMOUNT
    mlabel1=Label(mgui,text=mtext2).place(x=140,y=240)

mgui=Tk()     #OBJECT CREATION USING TKINTER

ment=IntVar()      #FOR STORING VARIABLE

ment2=IntVar()      #FOR STORING  SECOND VARIABLE
ment3=IntVar()      #FOR STORING  SECOND VARIABLE

mgui.geometry('400x400') #DIMENSION OF THE APP WHEN IT IS OPENED IN PIXEL 

mgui.title("SIMPLE INTERST CALCULATOR")   #TITLE OF THE APP

#FOR FIRST ENTRY ,BUTTON ,LABEL
mlabel=Label(mgui,text="Enter Principle").place(x=20,y=20)         #place is used to set the location   
mybutton=Button(mgui,text="Calculate",command=Calculate,fg="green",bg="red").place(x=20,y=300)

mENtry=Entry(mgui,textvariable=ment).place(x=120,y=20)     #grid, pack and sticky=E, E FOR EAST


#FOR SECOND ENTRY ,BUTTON ,LABEL

mlabel2=Label(mgui,text="Enter Rate").place(x=20,y=80)

mENtry=Entry(mgui,textvariable=ment2).place(x=120,y=80)



#FOR THIRD ENTRY ,LABEL

mlabel3=Label(mgui,text="Enter Time").place(x=20,y=140)

mENtry=Entry(mgui,textvariable=ment3).place(x=120,y=140)

#display result
mlabel=Label(mgui,text="Interst in Rs").place(x=40,y=200) # display of interst

mlabel=Label(mgui,text="Amount in Rs ").place(x=40,y=240)   # display of amount



mgui.mainloop()        #to close the main loop

