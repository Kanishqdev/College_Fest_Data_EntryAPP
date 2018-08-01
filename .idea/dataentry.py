from tkinter import *
import tkinter
import os
import sys
import csv
#import tkMessageBox
def information():
    def sayajin():
        l=[]
        with open("studentdetails.csv",'r') as csvfile:
            data=csv.reader(csvfile)
            for row in data:
                if(row[5]==ro_ll.get()):
                    l.append(row[0])
                    l.append(row[1])
                    l.append(row[2])
                    l.append(row[3])
                    l.append(row[4])
                    l.append(row[5])
                    break
            name.insert('1.0',l[0]+" "+l[1]+"\n")
            email1id.insert('1.0',l[2]+'\n')
            pho_ne.insert('1.0',(l[3])+'\n')
            works.insert('1.0',l[4]+'\n')
            csvfile.close()
    i=Tk()
    i.wm_title("Student Details")
    h2=Label(i,text="Student Details",font=("Helvetica",16)).grid(row=0,column=1)
    roll1=Label(i,text="Enter the roll no:").grid(row=1,column=0)
    ro_ll=Entry(i,bd=6)
    ro_ll.grid(row=1,column=1)
    rollBut=Button(i,text="GET IT",fg="red",command=sayajin).grid(row=2,column=1)
    n=Label(i,text="Name:",fg="#567874",pady=10).grid(row=3,column=0)
    name=Text(i,bd=6,height=1,width=22)
    name.grid(row=3,column=1)
    email1=Label(i,text="Email-Id:",fg="#567874",pady=10)
    email1.grid(row=4,column=0)
    email1id=Text(i,bd=5,height=1,width=22)
    email1id.grid(row=4,column=1)
    phone_num=Label(i,text="Phone No:",fg="#567874",pady=10).grid(row=5,column=0)
    pho_ne=Text(i,bd=6,height=1,width=22)
    pho_ne.grid(row=5,column=1)
    work=Label(i,text="Workshop Enrolled:",fg="#567874",pady=10).grid(row=6,column=0)
    works=Text(i,bd=6,height=1,width=22)
    works.grid(row=6,column=1)
    i.geometry("800x600")
    i.mainloop()
def newEntry():
    def new_Entry():
        j=0
        l=[]
        with open("studentdetails.csv","a",newline='') as csvfile:
            data=csv.writer(csvfile,delimiter=',')
            E1=fir.get()
            E2=sec.get()
            E3=email.get()
            E4=pho.get()
            E5=roll.get()
            E6=interest1.get()
            l.append(E1)
            l.append(E2)
            l.append(E3)
            l.append(E4)
            l.append(E6)
            l.append(E5)
            data.writerow(l)
            csvfile.close()
    e=Tk()
    e.wm_title("NEW ENTRY")
    h1=Label(e,text="Enter the following details.").grid(row=0,column=1)
    first=Label(e,text="First Name:").grid(row=1,column=0)
    second=Label(e,text="Second Name:").grid(row=2,column=0)
    emailId=Label(e,text="Valid email ID:").grid(row=3,column=0)
    phone=Label(e,text="Phone Number:").grid(row=4,column=0)
    roll=Label(e,text="Your JNTU Roll No:").grid(row=5,column=0)
    interest=Label(e,text="Enter interested Workshop:").grid(row=6,column=0)
    fir=Entry(e,bd=6)
    fir.grid(row=1,column=1)
    sec=Entry(e,bd=6)
    sec.grid(row=2,column=1)
    email=Entry(e,bd=6)
    email.grid(row=3,column=1)
    pho=Entry(e,bd=6)
    pho.grid(row=4,column=1)
    roll=Entry(e,bd=6)
    roll.grid(row=5,column=1)
    interest1=Entry(e,bd=6)
    interest1.grid(row=6,column=1)
    butSub=Button(e,text="Submit",fg="red",command=new_Entry).grid(row=7,column=0)
    e.geometry("400x300")
    e.mainloop()

root=Tk()
root.wm_title("Raghu Chakravyuh")
C=Canvas(root,bg="blue", height=720,width=1280)
backgroundimg=PhotoImage(file = "C:\\Users\\kanis\\OneDrive\\Desktop\\New folder\\bg1.png")
t=Canvas(root,bg="blue",height=720,width=1280)
bg1=PhotoImage(file="C:\\Users\\kanis\\OneDrive\\Desktop\\New folder\\LOGO1.png")
img=Label(root,image=backgroundimg)
img.place(x=0,y=0,relwidth=1,relheight=1)
top = Frame(root, width=520, height=400)
top.pack(side=TOP,expand=NO,fill=NONE)
l1=Label(top,text="DATA ENTRY",font=("Helvetica",15)).pack(pady=50)
newEntryBut=Button(top,text="NEW ENTRY",command=newEntry).pack(ipady=7,pady=50)
studentDetailsBut=Button(top,text="STUDENT DETAILS",command=information).pack(fill=X,ipady=8)
C.pack()
t.pack
root.mainloop()

