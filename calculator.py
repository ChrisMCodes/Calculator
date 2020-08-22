#!/usr/bin/env python3

#
# @author ChrisMCodes
#
# Date: 2020-08-21
#
# Purpose: A simple calculator app (in progress)

from tkinter import *
import sys

# Creating window
root = Tk()
root.title("Calculator")

# Creating grid
mainframe = Frame(root)
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 10)
mainframe.pack(pady = 5, padx = 5)

def on_click(*args):
    Label(mainframe, text="You clicked a button!").grid(row = 1)

# top row
seven = Button(mainframe, text="7", command=on_click).grid(row = 3, column = 1)
eight = Button(mainframe, text="8", command=on_click).grid(row = 3, column = 2)
nine = Button(mainframe, text="9", command=on_click).grid(row = 3, column = 3)

# middle row
four = Button(mainframe, text="4").grid(row = 5, column = 1)
five = Button(mainframe, text="5").grid(row = 5, column = 2)
six = Button(mainframe, text="6").grid(row = 5, column = 3)

# bottom row
one = Button(mainframe, text="1").grid(row = 7, column = 1)
two = Button(mainframe, text="2").grid(row = 7, column = 2)
three = Button(mainframe, text="3").grid(row = 7, column = 3)

root.mainloop()