import random

from tkinter import *
from tkinter import messagebox

from wordle_dictionary import words


class Word():
    """Gets the word randomnly chosen from the word list"""
    def __init__(self, word) -> None:
        self.word = word
    def get_word(self):
        """Returns a random word from word list containing words with letter count range 4-7"""
        self.word = random.choice(words.upper())

class LetterCount(Word):
    """Gets the randomnly selected word"""
    def __init__(self, word, letter_count) -> None:
        super().__init__(word)
        self.letter_count = letter_count

    def get_letter_count(self):
        """Returns letter count of the randomnly selected word"""
        self.letter_count = len(str(self.word))
        return self.letter_count
        
    
class DisplayCount(LetterCount):
    """Displays the letter  count of the randomly selected word to the user"""
    def __init__(self, word, letter_count) -> None:
        super().__init__(word, letter_count)
    def disp_cnt(self):
        """Displays the letter count of the chosen word"""
        print(f'Your word has {self.letter_count} letters')

class GuessEntry(LetterCount):
    """Prompts user to enter a word guess entry"""
    def __init__(self, word, letter_count, guess) -> None:
        super().__init__(word, letter_count)
        self.guess = guess
    def get_guess(self, word_entry):
        """Gets the user's guess from tkinter Entry widget"""
        self.guess = word_entry

class GuessCheck(GuessEntry):
    """Checks the user's guess"""
    def __init__(self, letter_count, word, guess) -> None:
        super().__init__(letter_count, word, guess)
        self.guess_cnt = 1
    def check_guess(self):
        """Checks each letter of the user's guess against the correct word. A turn is added to the turn count
        until the user uses 5 turns or guesses the correct word"""
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
        messagebox.showerror('Incorrect!', f'You lose! The correct word was {self.word}')
        
class Color(GuessEntry):
    """Evaluates the color of each letter per its degree of correctness"""
    def __init__(self, word, letter_count, guess) -> None:
        super().__init__(word, letter_count, guess)
    def color_change(self):
        """Changes the color of each letter of the user's guess. Green to indicate correct letter and placement, yellow for correct letter and wrong placement,
        and black for incorrect letter and placement"""
        for i, letter in enumerate(self.guess):
            label = Label(text=letter.upper())
            label.grid(row=GuessCheck.guess_cnt, column=i, padx=10, pady=10)
            if letter == self.word[i]:
                label.config(bg='green', fg='black')
            if letter in self.word and not letter == self.word[i]:
                label.config(bg='yellow', fg= 'black')
            if letter not in self.word:
                label.config(bg='black', fg='white')   

class CorrectWord(GuessEntry):
    """Displays the correct word when the user guesses the word correctly before running out of turns"""
    def __init__(self, word, letter_count, guess) -> None:
        super().__init__(word, letter_count, guess)
    def disp_correct_word(self):
        """Displays a congratulatory message and the correct word"""
        if self.guess == self.word:
            return f'Correct! The word was {self.word}!'
        