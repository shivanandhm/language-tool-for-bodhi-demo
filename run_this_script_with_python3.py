import tkinter
import subprocess

subprocess.call('./warn.sh', shell=True)

top = tkinter.Tk()
top.geometry("350x350")


def helloCallBack():
   subprocess.call('./s.sh', shell=True)

def ehelloCallBack():
   subprocess.call('./en.sh', shell=True)

def fhelloCallBack():
   subprocess.call('./s.sh', shell=True)

def thelloCallBack():
   subprocess.call('./te.sh', shell=True)

def shelloCallBack():
   subprocess.call('./slov.sh', shell=True)

B = tkinter.Button(top, text ="Spanish", width=45, height=2, command = helloCallBack)
B.pack()

a= tkinter.Button(top, text ="english", width=45, height=2, command = ehelloCallBack)
a.pack()

c= tkinter.Button(top, text ="french", width=45, height=2, command = fhelloCallBack)
c.pack()

d= tkinter.Button(top, text ="telugu", width=45, height=2, command = thelloCallBack)
d.pack()

e= tkinter.Button(top, text ="slovak", width=45, height=2, command = shelloCallBack)
e.pack()
top.mainloop()
