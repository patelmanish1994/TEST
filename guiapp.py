from Tkinter import*
parent =Tk()
##username = StringVar()
##name = Entry(parent, textvariable="username")
##name.pack()

parent.title("MY COMPANY WAGES CALCULATOR ")
parent.maxsize(800,800)
parent.configure(bg="blue")

l1 = Label(parent,text="HOURS OF WORKING")
l1.pack(side = LEFT)
E1=Entry(parent,bd=5,width=40)
E1.pack(side=LEFT)
