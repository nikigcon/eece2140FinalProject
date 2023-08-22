import random

from tkinter import *
from tkinter import messagebox

from wordle_dictionary import words

root = Tk()

class Word():
    """Gets the word randomnly chosen from the word list"""
    def __init__(self, word) -> None:
        self.word = word
    def get_word(self):
        """Returns a random word from word list containing words with letter count range 4-7"""
        self.word = random.choice(words)

class LetterCount(Word):
    """Gets the randomnly selected word"""
    def __init__(self, word, letter_count) -> None:
        super().__init__(word)
        self.letter_count = letter_count

    def get_letter_count(self):
        """Returns letter count of the randomnly selected word"""
        self.letter_count = len(self.word)
        return self.letter_count
        
    
class DisplayCount(LetterCount):
    def __init__(self, word, letter_count) -> None:
        super().__init__(word, letter_count)
    def disp_cnt(self):
        return f'Your word has {self.letter_count} letters'

class GuessEntry(LetterCount):
    def __init__(self, word, letter_count, guess) -> None:
        super().__init__(word, letter_count)
        self.guess = guess
    def get_guess(self):
        word_entry = Entry(root)
        word_entry.grid(row=999, column=0, padx=10, pady=10, columnspan=3)
        self.guess = word_entry.get()

class Guess(GuessEntry):
    def __init__(self, letter_count, word, guess) -> None:
        super().__init__(letter_count, word, guess)
        self.guess_cnt = 1
    def check_guess(self):
        self.guess_cnt += 1
        while self.guess_cnt <= 5:
            if len(self.guess) == self.letter_count:
                if self.guess == self.word:
                    CorrectWord.disp_correct_word()
                else:
                    Color.color_change()    
            else:
                messagebox.showerror(f'Please make sure your guess has {self.letter_count} letters.',f'Please make sure your guess has {self.letter_count} letters.')
                self.guess_cnt -= 1
        
class Color(GuessEntry):
    def __init__(self, word, letter_count, guess) -> None:
        super().__init__(word, letter_count, guess)
    def color_change(self):
        for i, letter in enumerate(self.guess):
            label = Label(text=letter.upper())
            label.grid(row=Guess.guess_cnt, column=i, padx=10, pady=10)
            if letter == self.word[i]:
                label.config(bg='green', fg='black')
            if letter in self.word and not letter == self.word[i]:
                label.config(bg='yellow', fg= 'black')
            if letter not in self.word:
                label.config(bg='black', fg='white')   

class CorrectWord(GuessEntry):
    def __init__(self, word, letter_count, guess) -> None:
        super().__init__(word, letter_count, guess)
    def disp_correct_word(self):
        if self.guess == self.word:
            return f'Correct! The word was {self.word}!'