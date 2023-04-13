import tkinter as tk
import mysql.connector
from gtts import gTTS
from tkinter import messagebox
from playsound import playsound
top = tk.Tk()
top.title("QnA chat")
top.config(bg = "light green")
top.geometry("500x500")
mydb = mysql.connector.connect(host = "localhost", user = "root", password = "root", database = "chatbox")
mycur = mydb.cursor()

newn = ""
name = 100000

def give_name():
    sp = T2.get()
    l = 'en'
    obj = gTTS(text = sp, lang = l, slow = False)
    global name
    global newn
    mycur.execute("select * from chat")
    result = mycur.fetchall()
    newf = ""
    for x in result:
        newf = x[0]
    newn = (str(name) + str(newf) + ".mp3")
    obj.save(newn)
    return newn
    
def validator(q, a):
    if(q == None or q == " "):
        messagebox.showinfo("Warning", "Please Enter Question.")
    if(a == None or a == " "):
        messagebox.showinfo("Warning", "Please enter Answer.")
    
def store():
    Q = T1.get()
    A = give_name()
    validator(Q, A)
    io = "insert into chat(Question, Answer)values(%s, %s)"
    value = (Q, A)
    mycur.execute(io, value)
    mydb.commit()
    messagebox.showinfo("QnA", "Data is successfully inserted..")
    
def play():
    playsound(newn)
        
def search():
    sq = T3.get()
    print("play with me")
    query = "select * from chat"
    mycur.execute(query)
    result = mycur.fetchall()
    isthere = False
    ans = ""
    for x in result:
        if(x[1] == sq):
            isthere = True
            ans = x[2]
    if(isthere):
        playsound(ans)
        
    
L1 = tk.Label(top, text = "Enter a Question:", bg = "light green", font =["", 15])
L1.place(x = 50, y = 150)

T1 = tk.Entry(top, font = ["", 15])
T1.place(x = 250, y = 150)

L2 = tk.Label(top, text = "Enter a Answer:", bg = "light green", font =["", 15])
L2.place(x = 50, y = 200)

T2 = tk.Entry(top, font = ["", 15])
T2.place(x = 250, y = 200)

B = tk.Button(text = "Store", font =["", 15], bg = "light green", command = store)
B.place(x = 220, y = 250)

B2 = tk.Button(text = "              Play              ", bg = "grey", font = ["", 15], command = play)
B2.place(x = 150, y = 310)

L3 = tk.Label(top, text = "Search Your Question Here.!", bg = "light green", font = ["", 15])
L3.place(x = 50, y = 375)

T3 = tk.Entry(top, font = ["", 15])
T3.place(x = 150, y = 410)

B3 = tk.Button(top, text = "Search", bg = "grey", font = ["", 15], command = search)
B3.place(x = 220, y = 450)

top.mainloop()
