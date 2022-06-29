import os
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sys
import PIL

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
    def __init__(self):


        self.window = Tk()
        self.window.attributes('-fullscreen', True)

        self.window.title("Print Verification")



        self.window.geometry('200x200')

        self.window.configure(bg="#330000")

        self.lbl = Label(self.window, text="Password:",bg="#330000",font=(25),fg="#FFD700")

        self.lbl.place(relx = .4, rely =.3,anchor=CENTER)

        self.txt = Entry(self.window,show = '*',font=(15))

        self.txt.place(relx = .5, rely =.35,anchor=CENTER,height=50, width=400)

        btn = Button(self.window, text="ENTER", command=self.clicked)

        canvas = tk.Canvas(self.window, width=300, height=300)

        login_btn = PhotoImage(file="rounded_button.png")

        # Create button and image
        img = Button(self.window, image=login_btn,
                     borderwidth=0,bg="#330000", text="ENTER", command=self.clicked)

        img.place(relx = 0.5, rely = 0.5,anchor=CENTER)


        self.window.mainloop()



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
            print("works")
def main():
    ob = ui()
if __name__ == "__main__":
    main()