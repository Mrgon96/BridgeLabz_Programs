from tkinter import *
top = Tk()
top.title("StopWatch")
top.geometry("400x500")
welcome = Text(top,"Welcome to Stopwatch")
startbutton = Button(top,text= "START",bg='black',fg ='lightgreen',width =10).place(x=150,y=100)
stopbutton = Button(top,text= "STOP",bg='black',fg ='red',width =10).place(x=150,y=150)
resetbutton = Button(top,text= "RESET",bg='black',fg ='yellow',width =10).place(x=150,y=200)
# redbutton.pack(side = TOP)
top.mainloop()




