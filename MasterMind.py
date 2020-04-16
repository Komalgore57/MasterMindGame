#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# To Start Game
def start():
    lbl.destroy()
    b1.destroy()
    b2.destroy()
    first(cmd=row)
    
    windows.mainloop()


# To Show Instruction
def ins():
    
    
    windows1= Tk()
    windows1.title("Mastermind")
    windows1.geometry('1000x700')
    windows1.config(bg='#02fff7')
    
    x="Colour scheme: green, red, yellow, blue, orange, purple.\nI'm thinking of a 4 colour code. Try and guess what it is!\nNote: duplicates are allowed.\nInput your guess like this: 'RRYB'.\nYou will then be awarded one or more black or white pegs.\nA black peg means right colour, right position.\nA white peg means right colour, wrong position.\nYou have 7 guesses. Good luck!"
    x=x.split("\n")
    a=200
    b=100
    Label(windows1, text='INSTRUCTION',font=("Arial Bold", 20), bg='#02fff7', fg='#000000').place(x=a,y=b)
    b+=50
    for i in x:
        b+=50
        Label(windows1, text=i,font=("Arial Bold", 10), bg='#02fff7', fg='#000000').place(x=a,y=b)

    windows.mainloop()
# To compare 
def check(num,res,a=100,y=500):

    l=[]
    z=0
    color=['Y','O','P','B','R','G']
    for i in res:
        if i not in color:
            print("Invalid")
            z=1
  
    w=0
    b=0

    if z==0:
        w=0
        b=0
        for i in range(0,4):
            if num[i]== res[i]:
                w+=1
        if w==4:
            print('Win')
        else:
            for i in res:    
                b+=num.count(i)   
    x=900
    Label(windows, text =str(w),bg="#ffffff",fg="#02e0ff",font=("Arial Bold", 10)).place(x=x,y=y)
    x=x+50
    Label(windows, text =str(b),bg="#000000",fg="#02e0ff",font=("Arial Bold", 10)).place(x=x,y=y)
    
def cmd(k):
    k()
def row2():
    row(x=100,y=500,cmd=row3)
def row3():
    row(x=100,y=450,cmd=row4)
def row4():
    row(x=100,y=400,cmd=row5)
def row5():
    row(x=100,y=350,cmd=row6)
def row6():
    row(x=100,y=300,cmd=row7)
def row7():
    row(x=100,y=250,cmd=row8)

def row8():
    final = Label(windows, text="You Loss !!",font=("Arial Bold", 20), bg='#1abc9c', fg='#ffffff')
    final.place(x=450,y=100)
    x=0
    for i in num:
        x+=100
        Label(windows, text=i,font=("Arial Bold", 10), bg='#1abc9c', fg='#ffffff').place(x=x,y=100)
    
def row(x=100,y=550,cmd=row2):
    
    def show_entry_fields():
        #print("First Name: %s\nLast Name: %s %s,%s" % (e1.get(), e2.get(),e3.get(),e4.get()))
        l=[e1.get().capitalize() , e2.get().capitalize() ,e3.get().capitalize() ,e4.get().capitalize() ]
        check(num,l,y=y)
        cmd()
    e1 = Entry(windows,width=3)
    e2 = Entry(windows,width=3)
    e3 = Entry(windows,width=3)
    e4 = Entry(windows,width=3)
    e1.place(x=x,y=y)
    x+=150
    e2.place(x=x,y=y)
    x+=150
    e3.place(x=x,y=y)
    x+=150
    e4.place(x=x,y=y)
    x+=150
    b1=Button(windows,text='Submit',font=("Arial Bold", 10), bg='#a04000', fg='#ffffff',command=show_entry_fields).place(x=x,y=y)
    x+=100
 
# Starting of first page
def first(y=650,cmd=row):

    v = StringVar(windows, "1") 

    # Dictionary to create multiple buttons 
    values = {"Red   " : "   R   ", 
                  "Green " : "   G   ", 
                  "Blue  " : "   B   ", 

                  "Purple" : "   P   ",
             "Yellow" : "   Y   ",
             "Orange":"   O   "}
    color =  {"Red   " : "#FF0000", 
                  "Green " : "#28b463", 
                  "Blue  " : "#5dade2", 

                  "Purple" : "#920c82",
                  "Yellow" : "#f7fa0d",
                 "Orange":"#ff9f02"}
    x=100
    
        # Loop is used to create multiple Radiobuttons 
        # rather than creating each button separately 
    for (text, value) in values.items(): 
        Label(windows, text =value,
        bg=color[text],fg="#000000",font=("Arial Bold", 10),).place(x=x,y=y)
        x+=100
   # b2=Button(windows,text='Next Move',font=("Arial Bold", 10), bg='#0052cc', fg='#ffffff',command=row).place(x=x,y=y)


        row()


# In[101]:





# In[ ]:






from tkinter import *

# To Generate Randome Pattern
import random 
num=[]
color=['Y','O','P','B','R','G']

for i in range(0,4):
    x = str(random.choice(color))
    num.append(x)



windows = Tk()
windows.title("Mastermind")
windows.geometry('1000x700')
windows.config(bg='#1abc9c')

lbl = Label(windows, text="MasterMind",font=("Arial Bold", 50), bg='#1abc9c', fg='#ffffff')
lbl.place(x=350,y=100)
x="INSTRUCTIONS:\nColour scheme: green, red, yellow, blue, orange, purple.\nI'm thinking of a 4 colour code. Try and guess what it is!\nNote: duplicates are allowed.\nInput your guess like this: 'RRYB'.\nYou will then be awarded one or more black or white pegs.\nA black peg means right colour, right position.\nA white peg means right colour, wrong position.\nYou have 7 guesses. Good luck!"
x=x.split("\n")
#g.place(x=200,y=50)
b1=Button(windows,text='Start The Game',font=("Arial Bold", 20), bg='#1abc9c', fg='#ecf0f1',command=start)
b1.place(x=400,y=300)
b2=Button(windows,text='Instruction Set',font=("Arial Bold", 20), bg='#1abc9c', fg='#ecf0f1',command=ins)
b2.place(x=400,y=500)
windows.mainloop()


# In[ ]:

