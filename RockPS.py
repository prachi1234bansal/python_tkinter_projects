from tkinter import *
from random import choice
root=Tk()
root.geometry("400x400")
root.title("Rock Paper Scissor")
l=Label(text="ROCK PAPER SCISSOR LETS GO TO PLAY",font="italic",bg="black",fg="dark blue",width=55,height=5)

def r1():
    #userChoice["text"]="User Choice is: Rock";
    comp_list=["Rock","Paper","Scissor"];
    comp_list_choice=choice(comp_list);
    comChoice["text"] = f"Computer Choice is {comp_list_choice}"
    r1["stat"] = "disabled";
    r2["stat"] = "disabled";
    r3["stat"] = "disabled";
    if comp_list_choice=="Rock":
        msg["text"]="It is draw";
    if comp_list_choice=="Paper":
        msg["text"]="Computer wins";
    if comp_list_choice=="Scissor":
        msg["text"]="User wins";

def r2():
    #userChoice["text"]="User choice is :Paper";
    comp_list=["Rock","Paper","Scissor"];
    comp_list_choice=choice(comp_list);
    comChoice["text"]=f"Computer Choice is {comp_list_choice}"
    r1["stat"] = "disabled";
    r2["stat"] = "disabled";
    r3["stat"] = "disabled";
    if comp_list_choice=="Rock":
        msg["text"]="User wins";
    if comp_list_choice=="Paper":
        msg["text"]="It is draw";
    if comp_list_choice=="Scissor":
        msg["text"]="Computer wins";

def r3():
    #userChoice["text"]="User Choice is :Scissor";
    comp_list=["Rock","Paper","Scissor"];
    comp_list_choice=choice(comp_list);
    comChoice["text"] = f"Computer Choice is {comp_list_choice}"
    r1["stat"]="disabled";
    r2["stat"]="disabled";
    r3["stat"]="disabled";
    if comp_list_choice=="Rock":
        msg["text"]="Computer wins";
    if comp_list_choice=="Paper":
        msg["text"]="User wins";
    if comp_list_choice=="Scissor":
        msg["text"]="It is draw";

def active():
    r1["stat"]="normal";
    r2["stat"]="normal"
    r3["stat"]="normal"
    msg["text"]=""
    comChoice["text"]=""
    userChoice["text"]="";

r1=Button(text="Rock",fg="black",bg="white",font="bold",width=40,height=3,relief="groove",command=r1)
r2=Button(text="Paper",fg="black",bg="white",font="bold",width=40,height=3,relief="groove",command=r2)
r3=Button(text="Scissor",fg="black",bg="white",font="bold",width=40,height=3,relief="ridge",command=r3)
active=Button(text="PLAY AGAIN!!",fg="white",bg="black",font="bold",width=40,height=3,relief="ridge",command=active)
l.pack();
r1.pack();
r2.pack();
r3.pack();
comChoice=Label(root,text="")
comChoice.pack();
msg=Label(root,text="",font=("Helvetica",17,"bold"))
msg.pack();
active.pack();
root.mainloop();