# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 12:21:32 2023

@author: Murat
"""
from random import randint
from tkinter import *

app=Tk()
app.configure(bg="black")
app.title("Butonu Kovala")
app.geometry("400x400")

S_seviyesi=100
M_seviyesi=100

def Oyna():
    mainframe.place_forget()
    btn1.place(x=175,y=175,height=50,width=50)
    btnanasayfa.place(x=380,y=0,height=20,width=20)
    
    
def Degistir():
    x=randint(10,330)
    y=randint(10,330)
    h=randint(30,50)
    w=randint(30,50)
    btn1.place(x=x,y=y,height=h,width=w)


def Anasayfa():
    mainframe.place(x=0,y=0,height=400,width=400)
    btnanasayfa.place_forget()
    btn.place(x=150,y=180,height=50,width=100)
    btn1.place_forget()
    ayarlarframe.place_forget()
    hakkindaframe.place_forget()


def Ayarlar():
    global sesentry, sesdegerientry, muzikdegerientry, muzikentry, S_seviyesi, M_seviyesi
    mainframe.place_forget()
    ayarlarframe.place(x=0,y=0,height=400,width=400)
    
    btnanasayfa.place(x=380,y=0,height=20,width=20)  #snake_case    camelCase
    
    seslbl=Label(ayarlarframe,bg="yellow",text="Ses Düzeyi")
    seslbl.place(x=50,y=60,height=20,width=60)
    muziklbl=Label(ayarlarframe,bg="yellow",text="Müzik sesi")
    muziklbl.place(x=50,y=95,height=20,width=60)
    
    sesdegerientry=Entry(ayarlarframe,bg="yellow")
    sesdegerientry.insert(0, S_seviyesi)
    sesdegerientry["state"]="disabled"
    sesdegerientry.place(x=120,y=60,height=20,width=20)
    
    muzikdegerientry=Entry(ayarlarframe,bg="yellow")
    muzikdegerientry.insert(0, M_seviyesi)
    muzikdegerientry["state"]="disabled"
    muzikdegerientry.place(x=120,y=95,height=20,width=20)
    
    sesentry=Entry(ayarlarframe,bg="yellow")
    sesentry.place(x=145,y=60,height=20,width=20)
    
    muzikentry=Entry(ayarlarframe,bg="yellow")
    muzikentry.place(x=145,y=95,height=20,width=20)
    
    sesonaybutonu=Button(ayarlarframe,bg="yellow",text="✓",command=Sesdegistir)
    sesonaybutonu.place(x=170,y=60,height=20,width=20)
    
    muzikonaybutonu=Button(ayarlarframe,bg="yellow",text="✓",command=Muzikdegistir)
    muzikonaybutonu.place(x=170,y=95,height=20,width=20)
    
    
def Sesdegistir():
    global S_seviyesi
    sesdegerientry["state"]="normal"
    sesdegerientry.delete(0, END)
    ses=int(sesentry.get())
    S_seviyesi=ses
    sesdegerientry.insert(END, sesentry.get())
    sesdegerientry["state"]="disabled"
    
def Muzikdegistir():
    global M_seviyesi
    muzikdegerientry["state"]="normal"
    muzikdegerientry.delete(0, END)
    muzik=int(muzikentry.get())
    M_seviyesi=muzik
    muzikdegerientry.insert(END, muzikentry.get())
    muzikdegerientry["state"]="disabled"
    
    
def Hakkinda():
    mainframe.place_forget()
    hakkindaframe.place(x=0,y=0,height=400,width=400)
    hakkindalbl=Label(hakkindaframe,bg="yellow",text="Oyunu yapan ve tasarlayan: Murat Göçmen",anchor="w")
    hakkindalbl.place(x=55,y=60,height=20,width=300)
    hakkindalbl=Label(hakkindaframe,bg="yellow",text="Yardımcıları: Hamza Eren Sarpdağ, Berk Gündüz",anchor="w")
    hakkindalbl.place(x=55,y=80,height=20,width=300)
    hakkindalbl=Label(hakkindaframe,bg="yellow",text="Muhammed Utku Aksu, Veysel Tandoğru, Enes Mergen",anchor="w")
    hakkindalbl.place(x=55,y=100,height=20,width=300)
    btnanasayfa.place(x=380,y=0,height=20,width=20)

mainframe=Frame(app,bg="black")
mainframe.place(x=0,y=0,height=400,width=400)

ayarlarframe=Frame(app,bg="Black")

hakkindaframe=Frame(app,bg="black")

btn1=Button(app,text="Tıkla",command=Degistir)

btnanasayfa=Button(app,text="X",bg="red",command=Anasayfa)

btn=Button(mainframe,text="oyna",command=Oyna)
btn.place(x=150,y=180,height=50,width=100)

btnayarlar=Button(mainframe,text="Ayarlar",command=Ayarlar)
btnayarlar.place(x=150,y=240,height=50,width=100)

btnhakkinda=Button(mainframe,text="Hakkında",command=Hakkinda)
btnhakkinda.place(x=150,y=300,height=50,width=100)







app.mainloop()