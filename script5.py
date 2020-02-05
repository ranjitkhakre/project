
import tkinter as tk
from tkinter import *

# Set up our GUIs
root = Tk()
w = Label(root, text="My Program")
w.pack()

# Welcome the user
tkMessageBox.showinfo("welcome", "Add your welcome message here.")

# Get user info
name = tkSimpleDialog.askstring("Name", "What is your name?")
age = tkSimpleDialog.askinteger("Age", "How old are you?")

# Process information
output = "Hello, %s. I hope you're doing fine today. " %(name)
output += "\nOur records indicate that you are %d years old." %(age)

# Produce the Output
tkMessageBox.showinfo("Results", output)