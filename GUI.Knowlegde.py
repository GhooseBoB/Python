from tkinter import *
from tkinter import ttk
from tkinter import messagebox
GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')
B1 = ttk.Button(GUI,text='เงินมีอยู่กี่่บาท')
B1.pack(ipadx=20,ipady=20)
def Botton2():
    text = 'ตอนนี้ฉันมีเงินอยู่300บาท'
    messagebox.showwarning('เงินในบัญชี',text)

FB1 = Frame(GUI)
FB1.place(x=100,y=300)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่่บาท',command=Botton2)
B2.pack(ipadx=20,ipady=20)

GUI.mainloop()


def Botton2():
    text = 'ตอนนี้ฉันมีเงินอยู่300บาท'
    message.showinfo('เงินในบัญชี',text)
