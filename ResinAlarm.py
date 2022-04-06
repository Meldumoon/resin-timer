import time
from tkinter import *
import webbrowser

root = Tk()
root.title("Resin Alarm")

def myClick():
    myLabel = Label(root,text="Your current resin value is: " + e.get())
    myLabel.grid(row=2,column=0)
    i = int(e.get())
    while i < 160:
        print(i)
        i +=1
        time.sleep(480)
        new_res_val = i
        if i == 160:
            webbrowser.open("https://www.youtube.com/watch?v=cu9EYHjohp0")
            

e = Entry(root)
myButton = Button(root, text="submit and start timer", command=myClick)

e.grid(row=0,column=0)
myButton.grid(row=1,column=0)
    

root.mainloop()