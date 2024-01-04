from tkinter import*
from tkinter import messagebox

parent = Tk(className='Voting Form ')
parent.geometry("1200x1200")

voting=Label(parent,text="Online Voting Commission",fg="red",font="150").place(x=440,y=10)

Candidatename=Label(parent,text="Candidate Name :",font="70").place(x=380,y=90)
e1=Entry(parent).place(x=540,y=90)

Candidateward=Label(parent,text="Candidate Ward :",font="70").place(x=380,y=130)
sb = Scrollbar(parent)  
sb.place(x=670,y=130)   
  
mylist = Listbox(parent, yscrollcommand = sb.set )    
for line in range(60):  
    mylist.insert(END, "Ward No -   " + str(line))  
  
mylist.place(x=540,y=130)  
sb.config( command = mylist.yview )

Candidatarea=Label(parent,text="Candidate Area :",font="70").place(x=380,y=310)
listbox = Listbox(parent)  
listbox.insert(1,"Thiruvarumbur")  
listbox.insert(2, "Thillai Nagar")  
listbox.insert(3, "Kattur")  
listbox.insert(4, "worayur")
listbox.insert(5, "K.K.Nagar ")
listbox.insert(6, "Thennur")
listbox.insert(7, "Anna Nagar")
listbox.insert(8, "Sri Rangam")

listbox.place(x=540,y=310)  


Votingparties=Label(parent,text=" Voting Parties :",font="70").place(x=380,y=490)


def fun():
    messagebox.showinfo("Hello","Voting successfull")
    
submitButton=Button(parent,text="DMK",command=fun,activeforeground="red",activebackground="pink").place(x=540,y=490)
submitButton1=Button(parent,text="ADMK",command=fun,activeforeground="red",activebackground="pink").place(x=540,y=520)
submitButton2=Button(parent,text="AMMK",command=fun,activeforeground="red",activebackground="pink").place(x=540,y=550)
submitButton3=Button(parent,text="BJP",command=fun,activeforeground="red",activebackground="pink").place(x=540,y=580)
submitButton4=Button(parent,text="DMDK",command=fun,activeforeground="red",activebackground="pink").place(x=540,y=610)


def fun1():
    messagebox.showinfo("Hello","Submission Successfull")
    
submitButton5=Button(parent,text="Submit",command=fun1,activeforeground="red",activebackground="pink").place(x=380,y=640)

def fun2():
    messagebox.showinfo("Hello","Submission Cancel")
    
submitButton6=Button(parent,text="Cancel",command=fun2,activeforeground="red",activebackground="pink").place(x=380,y=670)

parent.mainloop()
