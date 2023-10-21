from tkinter import *

window=Tk()
window.title("NTEREST CLACULATOR")
window.geometry("500x500")
window.configure(background="Green")

def calculateInt():
    p=float(pEnt.get())
    r=float(rEnt.get())
    t=float(tEnt.get())

    

    i=(p*r*t)/100
    i=round(i,2)
    result["text"]=i

titleLabel=Label(window,text="INTEREST CALCULATOR APP",bg="darkgreen",fg="lightgreen",font=("Adobe Garamond Pro Bold",14))
titleLabel.place(relx=0.5,rely=0.1,anchor=CENTER)

tLabel=Label(window,text="Enter Time:")
tLabel.place(relx=0.34,rely=0.25,anchor=CENTER)

pLabel=Label(window,text="Enter Principle:")
pLabel.place(relx=0.35,rely=0.35,anchor=CENTER)

rLabel=Label(window,text="Enter Rate:")
rLabel.place(relx=0.35,rely=0.45,anchor=CENTER)

tEnt=Entry(window)
tEnt.place(relx=0.55,rely=0.25,anchor=CENTER)

pEnt=Entry(window)
pEnt.place(relx=0.55,rely=0.35,anchor=CENTER)

rEnt=Entry(window)
rEnt.place(relx=0.55,rely=0.45,anchor=CENTER)




calculate=Button(window,text="Calculate!",command=calculateInt)
calculate.place(relx=0.5,rely=0.6,anchor=CENTER)


resultFrame=LabelFrame(window,text="RESULT")
resultFrame.place(relx=0.5,rely=0.7,anchor=CENTER)

result=Label(resultFrame,text="",width=40)
result.pack()

window.mainloop()