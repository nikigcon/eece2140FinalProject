from tkinter import *
from tkinter import messagebox
from wordle_dictionary import words
from wordle_functions import *
from wordle_gui import *


root = Tk()
root.title('WORDLE')

word_entry = Entry(root)
word_entry.grid(row=999, column=0, padx=10, pady=10, columnspan=3)
guess = word_entry.get()
Game.play(None, guess)

guessButton = Button(root, text='Guess', command=Game.play)
guessButton.grid(row=99, column=3, columnspan=2)

root.mainloop()


