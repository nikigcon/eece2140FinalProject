from tkinter import *
from wordle_functions import *


class Game(DisplayCount, GuessEntry):
    """Graphical User Interface logic of Wordle Game"""
    def __init__(self, word, letter_count, root, game) -> None:
        super().__init__(word, letter_count)
        self.root = root
        self.game = game
        

    def play(self, guess):
        """Presents user with letter count and proceeds with a pop-up window where the user can enter their guesses"""
        Word.get_word
        LetterCount.get_letter_count
        DisplayCount.disp_cnt
        GuessCheck.check_guess(guess)
    

