import tkinter as tk
from tkinter import *
from tkinter import messagebox as msgbox
import webbrowser

#form
form = tk.Tk()
form.title('Application')
form.configure(background='white')

#Function
def close():
	msg=msgbox.askquestion('Exit Application','Are you sure you want to exit?')
	if msg=='yes':
		form.destroy()

def openfb():
	webbrowser.open('https://www.facebook.com/komal.sinha.9275')

def home():
	f2=Frame(form,height=500,width=800,bg='white')
	l4=Label(f2,text='Get Started With Our',font=("Ubuntu", 42), width=38, bg='white')
	l5=Label(f2,text='© 2020 - Komal',font=("Ubuntu", 12), width=30, bg='white')
	l6=Label(f2,text='Language Translator',font=("Ubuntu", 30), width=35, bg='white')
	b5=Button(f2,image=fb_btn,command=openfb,borderwidth=0)
	l8=Label(f2,image=logo1)
	
	#pack
	f2.pack()
	l4.pack()
	l5.pack()
	l6.pack()
	b5.pack()
	l8.pack()

	#place
	f2.place(x=200,y=0)
	l4.place(x=-160,y=30)
	l5.place(x=250,y=440)
	l6.place(x=40,y=100)
	b5.place(x=330,y=460)
	l8.place(x=320,y=180)
	

def search():
	top1=Toplevel()
	top1.title('Search')
	top1.configure(background='white')
	top1.minsize(800,400)
	top1.resizable(0,0)
	top1.mainloop()

	

	
#color
color1= '#%02x%02x%02x' % (51,0,26) #purple

#Images
fb_btn=PhotoImage(file='facebook.png')
logo1=PhotoImage(file='logo.png')

#widgets
l1=Label(form,text='Get Started With Our',font=("Ubuntu", 42), width=38, bg='white')
l3=Label(form,text='Language Translator',font=("Ubuntu", 30), width=35, bg='white')
f1=Frame(form,bg=color1,bd=2,height=600,width=200)
l2=Label(form,text='© 2020 - Komal',font=("Ubuntu", 12), width=30, bg='white')
b1=Button(form,text='Exit',command=close,font=("Ubuntu", 11), height=2, width=20, fg='white', bg=color1, relief=GROOVE)
b2=Button(form,image=fb_btn,command=openfb,borderwidth=0)
b3=Button(form,text='Home',command=home,font=("Ubuntu", 11), height=2, width=20, fg='white', bg=color1, relief=GROOVE)
b4=Button(form,text='Search',command=search,font=("Ubuntu", 11), height=2, width=20, fg='white', bg=color1, relief=GROOVE)
l7=Label(form,image=logo1)

#Pack
f1.pack()
l1.pack()
l2.pack()
l3.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
l7.pack()

#Place
f1.place(x=0,y=0)
l1.place(x=40,y=30)
l2.place(x=450,y=440)
l3.place(x=240,y=100)
b1.place(x=3,y=290)
b2.place(x=530,y=460)
b3.place(x=3,y=150)
b4.place(x=3,y=220)
l7.place(x=520,y=180)


#form_properties
form.minsize(1000,500)
form.resizable(0,0)
form.mainloop()













