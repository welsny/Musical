__author__ = 'lola'

import tkinter
from tkinter import messagebox
import Identifier as id

win = tkinter.Tk()
win.title('Chord Identifier')

r1 = tkinter.Frame(win)
# Entry box for first person's name.
label = tkinter.Label(r1,text='Chord: ',font=("Courier New",10))
entry = tkinter.Entry(r1)

r2 = tkinter.Frame(win)
#infoButton
#identifyButton

def spaceLabel(parent):
    label = tkinter.Label(parent,text="    ",font=("Courier New",10))
    label.pack(side='left')

def spaceRow():
    newRow = tkinter.Frame(win)
    label = tkinter.Label(text=" ")
    label.pack()
    newRow.pack()

def identify_button_pressed():
    user_input = entry.get()

    result = id.identify(user_input)

    tkinter.messagebox.showinfo('Results', result+" ")


infoButton = tkinter.Button(r2,text= " help ", font=("Courier New",10),
                            command= lambda:
                            tkinter.messagebox.showinfo('Chord Identifier by WellSea',
                                                        "This program identifies musical chords from strings of notes"
                                                        " and guitar tabs. \n\n"
                                                        "Ex:\n 'CEG' = C Maj\n 'x21202' = B dom7"))

identifyButton = tkinter.Button(r2,text=" IDENTIFY ", command=identify_button_pressed, font=("Courier New",10))

spaceRow()

spaceLabel(r1)
label.pack(side='left')
entry.pack(side='left')
spaceLabel(r1)
r1.pack()

spaceRow()

infoButton.pack(side='left')
spaceLabel(r2)
identifyButton.pack(side='right')
r2.pack()

spaceRow()

win.mainloop()