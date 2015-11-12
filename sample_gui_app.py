from tkinter import messagebox
from tkinter import *
from identifier import *

win = Tk()
win.title('Chord Identifier')

r1 = Frame(win)
# Entry box for first person's name.
label = Label(r1,text='Chord: ',font=("Courier New",10))
entry = Entry(r1)

r2 = Frame(win)
#infoButton
#identifyButton

def space_label(parent):
    label = Label(parent,text="    ",font=("Courier New",10))
    label.pack(side='left')

def space_row():
    newRow = Frame(win)
    label = Label(text=" ")
    label.pack()
    newRow.pack()

def identify_button_pressed():
    user_input = entry.get()

    result = identify(user_input)

    messagebox.showinfo('Results', result+" ")


infoButton = Button(r2,text= " help ", font=("Courier New",10),
                            command= lambda:
                            messagebox.showinfo('Chord Identifier by WellSea',
                                                        "This program identifies musical chords from strings of notes"
                                                        " and guitar tabs. \n\n"
                                                        "Ex:\n 'CEG' = C Maj\n 'x21202' = B dom7"))

identifyButton = Button(r2,text=" IDENTIFY ", command=identify_button_pressed, font=("Courier New",10))

space_row()

space_label(r1)
label.pack(side='left')
entry.pack(side='left')
space_label(r1)
r1.pack()

space_row()

infoButton.pack(side='left')
space_label(r2)
identifyButton.pack(side='right')
r2.pack()

space_row()

win.mainloop()