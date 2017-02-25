#THIS PROGRAM CALCULATES SIMPLE INTERST ONLY WHEN ALL VALUE ENTERED ARE NUMERIC.
#OTHERWISE EVERY VALUE IS TO BE ENETERED AGAIN.

def EnterValue():                      #function for taking input.
    Principle= raw_input("Enter the Principle: ") 
    Rate= raw_input("Enter the RATE: ")
    Time= raw_input("Enter the TIME: ")
    
    #check wheather the entered value is integer or not
    if (Principle.isdigit()and Rate.isdigit()and Time.isdigit())==True:
        
        Interst=float(int(Principle)*int(Rate)*int(Time))/100           #Calculate interst.
        
        Amount=Interst+int(Principle)                                 #Calculate amount.
        
        print "Interst is : ",Interst
        print "Amount to be paid is :",Amount

        print "Interst  is calculated sucessfully"       #sucessfully excution of above code.


    if (Principle.isdigit()and Rate.isdigit()and Time.isdigit())==False:
        print "\nYou have enetered something wrong value CHECK IT "    
        print "Enter all values again."
        
        EnterValue()                    #call EnterValue function again if  ANY value is non numerical.
    

                                       
EnterValue()    #call EnterValue function first time 
                      
                                            


