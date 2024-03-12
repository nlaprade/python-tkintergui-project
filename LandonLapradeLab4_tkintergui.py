# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import font as tkFont
from tkinter import ttk
import tkinter.messagebox 

window = tk.Tk()
window.title("Centennial College")
window.geometry("425x325")
window.configure(bg='#55b4b0')

def resetButton():
    print("Reseting...")
    
    fNameEntry.delete(0, tk.END)
    fNameEntry.insert(0, originalValues['fName'])
    
    radioVar.set(originalValues['radioVar'])
    
    programCombobox.set(originalValues['progVar'])
    
    checkVar1.set(originalValues['checkVar1'])
    checkVar2.set(originalValues['checkVar2'])
    checkVar3.set(originalValues['checkVar3'])

def okButton():
    fullNameSelection = fNameEntry.get()
    radioButtonSelection = radioVar.get()
    programSelection = progVar.get()

    courseSelection = []
    if checkVar1.get() == 'COMP100':
        courseSelection.append("(COMP100)")
    if checkVar2.get() == 'COMP213':
        courseSelection.append("(COMP213)")
    if checkVar3.get() == 'COMP120':
        courseSelection.append("(COMP120)")
    courses = ", ".join(courseSelection)

    message = f"{fullNameSelection}\n{programSelection}\n{radioButtonSelection}\n{courses}"
    tkinter.messagebox.showinfo("Information", message)

def exitButton():
    print("Exiting...")
    window.destroy()

customFont = tkFont.Font(family="Helvetica", size=15, weight="bold", slant="italic")

surveyLabel = tk.Label(window, text="ICET Student Survey", font=customFont, bg='#55b4b0')
surveyLabel.grid(row=0, column=0, columnspan=2, sticky='ew')

window.grid_columnconfigure(0, weight=0)
window.grid_columnconfigure(1, weight=2)

# Full name label
fName = tk.Label(window, text="Full Name:", bg='#55b4b0')
fName.grid(row=1, column=0, sticky='w', padx=5, pady=5)

# Full name text box
fNameEntry = tk.Entry(window, width=30)
fNameEntry.grid(row=1, column=1, padx=(50,5), pady=5, sticky='w')
fNameEntry.insert(0, 'Narendra Pershad')

# Residency label
residencyLabel = tk.Label(window, text="Residency:", bg='#55b4b0')
residencyLabel.grid(row=2, column=0, sticky='w', padx=5, pady=5)

# Radio buttons
radioVar = tk.StringVar(value='dom')

domRes = tk.Radiobutton(window, text='Domestic', variable=radioVar, value='dom', bg='#55b4b0')
domRes.grid(row=2, column=1, padx=(50, 5), pady=5, sticky='w')

intRes = tk.Radiobutton(window, text='International', variable=radioVar, value='intl', bg='#55b4b0')
intRes.grid(row=3, column=1, padx=(50, 5), pady=5, sticky='w')

# Program text label
programLabel = tk.Label(window, text="Program:", bg='#55b4b0')
programLabel.grid(row=4, column=0, padx=5, pady=5, sticky='w')

# Program combobox
choices = ['AI', 'Gaming', 'Health', 'Software']
progVar = tk.StringVar()
programCombobox = ttk.Combobox(window, textvariable=progVar, values=choices, width=15, state='readonly')
programCombobox.grid(row=4, column=1, padx=(50,5), pady=5, sticky='w')
programCombobox.set('Health')

coursesLabel = tk.Label(window, text="Courses:", bg='#55b4b0')
coursesLabel.grid(row=5, column=0, sticky='w', padx=5, pady=5)

checkVar1 = tk.StringVar(value='COMP100')
checkVar2 = tk.StringVar(value='')
checkVar3 = tk.StringVar(value='')

progCheck = tk.Checkbutton(window, text='Programming I', variable = checkVar1, onvalue = 'COMP100', offvalue='', bg='#55b4b0')
progCheck.grid(row=5, column=1, padx=(50,5), pady=5, sticky='w')

webCheck = tk.Checkbutton(window, text='Web Page Design', variable = checkVar2, onvalue = 'COMP213', offvalue='', bg='#55b4b0')
webCheck.grid(row=6, column=1, padx=(50,5), pady=5, sticky='w')

softCheck = tk.Checkbutton(window, text='Software Engineering', variable = checkVar3, onvalue = 'COMP120', offvalue='', bg='#55b4b0')
softCheck.grid(row=7, column=1, padx=(50,5), pady=5, sticky='w')

# Buttons
frameB = tk.Frame(window, bg='#55b4b0')
frameB.grid(row=9, column=0, columnspan=2, pady=10)

button_width = 15

resetB = tk.Button(frameB, text="Reset", command=resetButton, width=button_width)
resetB.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

okB = tk.Button(frameB, text="Ok", command=okButton, width=button_width)
okB.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

exitB = tk.Button(frameB, text="Exit", command=exitButton, width=button_width)
exitB.grid(row=0, column=2, padx=5, pady=5, sticky="ew")

originalValues = {
    'fName': 'Narendra Pershad',
    'radioVar': 'dom',
    'progVar': 'Health',
    'checkVar1': 'COMP100',
    'checkVar2': '',
    'checkVar3': ''}

window.mainloop()