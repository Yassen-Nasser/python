from tkinter import *

panel= Tk()


panel.title('get name and age')
panel.minsize(300,300)
number1Label = Label ( text = "first Namber", fg="green", font = "Verdana 12 ")
number1Label.pack()
number1Entry = Entry()
number1Entry.pack()


number2Label = Label ( text = "last Namber", fg="green", font = "Verdana 12 ")
number2Label.pack()
number2Entry = Entry()
number2Entry.pack()

def addnum():

    num1 = int (number1Entry.get())
    num2 = int (number2Entry.get())
 
    res = num1 + num2
    resultlabel=Label(text="the result is :" + str(res))
    resultlabel.pack()
def subtract():
    num1 = int (number1Entry.get())
    num2 = int (number2Entry.get())
    res = num1 -num2
    resultlabel=Label(text="the result is :" + str(res))
    resultlabel.pack()
def multiply():
    num1 = int (number1Entry.get())
    num2 = int (number2Entry.get())
    res = num1 * num2
    resultlabel=Label(text="the result is :" + str(res))
    resultlabel.pack()
def dividion():
    num1 = int (number1Entry.get())
    num2 = int (number2Entry.get())
    res = num1 / num2
    resultlabel=Label(text="the result is :" + str(res), fg="green", font = "Verdana 12 "   )
    resultlabel.pack()




sumBtn = Button(text = "Sum" , command=addnum)
sumBtn.pack()
subtractBtn = Button(text = "Subtract" , command=subtract)
subtractBtn.pack()
multyplyBtn  = Button(text = "Multiply" , command=multiply)
multyplyBtn.pack()
dividBtn = Button(text = "Divided" , command=dividion)
dividBtn.pack()

panel.mainloop()






