from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root=Tk()
root.geometry("1000x1200")
root.title("World Clock")

ind = ImageTk.PhotoImage(Image.open("india.jpg"))
us = ImageTk.PhotoImage(Image.open("usa.jpg"))
aus = ImageTk.PhotoImage(Image.open("australia.jpg"))
jpn = ImageTk.PhotoImage(Image.open("japan.jpg"))


ind_l = Label(root,text="India")
ind_l.place(relx=0.2,rely=0.05, anchor= CENTER)
 
ind_c=Label(root)
ind_c["image"]=ind
ind_c.place(relx=0.2,rely=0.23, anchor= CENTER)
 
indt = Label(root)
indt.place(relx=0.2,rely=0.4, anchor= CENTER)
 
usl = Label(root,text="USA")
usl.place(relx=0.7,rely=0.05,anchor= CENTER)
 
usc=Label(root) 
usc.place(relx=0.7,rely=0.23, anchor= CENTER)
usc["image"]=us
 
ust = Label(root)
ust.place(relx=0.7,rely=0.4, anchor= CENTER)
#australia n japan

aus_l = Label(root,text="Australia")
aus_l.place(relx=0.2,rely=0.5, anchor= CENTER)
 
aus_c=Label(root)
aus_c["image"]=aus
aus_c.place(relx=0.2,rely=0.67, anchor= CENTER)
 
aus_t = Label(root, text="")
aus_t.place(relx=0.2,rely=0.85, anchor= CENTER)
 
jpnl = Label(root,text="Japan")
jpnl.place(relx=0.7,rely=0.5,anchor= CENTER)
 
jpnc=Label(root) 
jpnc.place(relx=0.7,rely=0.67, anchor= CENTER)
jpnc["image"]=jpn
 
jpnt = Label(root, text = "")
jpnt.place(relx=0.7,rely=0.85, anchor= CENTER)

class India():
    def time(self):
        tz = pytz.timezone("Asia/Kolkata")
        ct = datetime.now(tz)
        print(ct)
        convert = ct.strftime("%H:%M:%S")
        indt["text"] = "Time: " + convert
        indt.after(100,self.time)
    
class USA():
    def time(self):
        tz = pytz.timezone("US/Central")
        ct = datetime.now(tz)
        print(ct)
        convert = ct.strftime("%H:%M:%S")
        ust["text"] = "Time: " + convert
        ust.after(100,self.time)
        
class austr():
    def time(self):
        tz = pytz.timezone("Australia/ACT")
        ct = datetime.now(tz)
        print(ct)
        convert = ct.strftime("%H:%M:%S")
        aus_t["text"] = "Time: " + convert
        aus_t.after(100,self.time)
    
class Japan():
    def time(self):
        tz = pytz.timezone("Japan")
        ct = datetime.now(tz)
        print(ct)
        convert = ct.strftime("%H:%M:%S")
        jpnt["text"] = "Time: " + convert
        jpnt.after(100,self.time)
        

inda = India()
usaa = USA()
austt = austr()
jpntt = Japan()

indb = Button(root, text = "Show Time", command = inda.time)
indb.place(relx = 0.2, rely = 0.45, anchor = CENTER)

usb = Button(root, text = "Show Time", command = usaa.time)
usb.place(relx = 0.7, rely = 0.45, anchor = CENTER)

ausb = Button(root, text = "Show Time", command = austt.time)
ausb.place(relx = 0.2, rely = 0.9, anchor = CENTER)

jpnb = Button(root, text = "Show Time", command = jpntt.time)
jpnb.place(relx = 0.7, rely = 0.9, anchor = CENTER)

root.mainloop()