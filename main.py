import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sys
import datetime


class postProc:
    def __init__(self):
        self.printTime=600
    # def pp():
    #     sourceFile = sys.argv[0]
    #
    #     # Read the ENTIRE g-code file into memory
    #     with open(sourceFile, "r") as f:
    #         lines = f.readlines()
    #
    #     with open(sourceFile, "w") as of:
    #         for lIndex in range(len(lines)):
    #             oline = lines[lIndex]
    #             # Parse gcode line
    #             parts = oline.split(';', 1)
    #             if len(parts) > 0:
    #                 # Parse command
    #                 command = parts[0].strip()
    #
    #                 if command:
    #                     stringMatch = re.search('^M112', command)
    #                     if stringMatch:
    #                         # Insert code to bump fan to max before fan speed commands
    #                         of.write('\n')
    #
    #                 # Write original line
                    #of.write(oline)
    from PIL import ImageTk


class ui():
    def __init__(self,proc):
        self.proc=proc

        self.window = Tk()
        self.window.attributes('-fullscreen', True)

        self.window.title("Print Verification")

        self.window.geometry('200x200')

        self.window.configure(bg="#330000")

        self.lbl = Label(self.window, text="Password:",bg="#330000",font=(25),fg="#FFD700")

        self.lbl.place(relx = .4, rely =.3,anchor=CENTER)

        self.txt = Entry(self.window,show = '*',font=(15))

        self.txt.place(relx = .5, rely =.35,anchor=CENTER,height=50, width=400)

        login_btn = PhotoImage(file="rounded_button.png")

        # Create button and image
        img = Button(self.window, image=login_btn,
                     borderwidth=0,bg="#330000", text="ENTER", command=self.clicked)

        img.place(relx = 0.5, rely = 0.5,anchor=CENTER)

        exit_button = Button(self.window, text="Exit", command=self.on_closing)

        exit_button.place(relx = .5, rely =.7,anchor=CENTER,height=50, width=200)

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.window.mainloop()


    def on_closing(self):#iff the user exits I want to send -1 code so the gcode is cancled
        self.window.destroy()
        sys.exit(-1)

    def clicked(self):
        self.res = self.txt.get()
        self.checkPass()

    def checkPass(self):
        password = "password"
        if self.res != password:
            messagebox.showerror('Incorrect Password', 'Incorrect Password')
            self.window.destroy()
            sys.exit(-1)
        else:
            self.checkTime(self.proc)
            print("works")

    def checkTime(self,proc):
        time = int(datetime.datetime.now().strftime("%H"))
        print(time)
        if datetime.datetime.now().weekday():#checks if it is a weekday
            if time > 3:#check to see if it after 5pm
                if proc.printTime > 500: #checks if the print is under 12hours
                    self.open_popup("Print time  exceeds allowed time requirement")
            else:
                if proc.printTime > 500: #checks if the print is under 12hours
                    print("error")

    def open_popup(self,msg):
        top = Toplevel(self.window)
        top.focus_force()
        top.geometry("2000x2000")
        top.configure(bg="#330000")
        top.title("Override")

        Label(top, text="Your Print falls outside of normal parameters. " + msg,fg="gold",bg="#330000").place(x=150, y=10)

        lbl = Label(top, text="Password:", bg="#330000", font=(25), fg="#FFD700")

        lbl.place(relx=.4, rely=.3, anchor=CENTER)

        txt = Entry(top, show='*', font=(15))

        txt.place(relx=.5, rely=.35, anchor=CENTER, height=50, width=400)

        ###

        login_btn = PhotoImage(file="rounded_button.png")
        img = Button(top, image=login_btn,borderwidth=0, bg="#330000", text="ENTER")
        img.place(relx=0.5, rely=0.5, anchor=CENTER)



def main():
    proc=postProc()
    ob = ui(proc)
if __name__ == "__main__":
    main()