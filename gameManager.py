import tkinter
from homePage import Home_page
from wordSearch import Word_Search
from sudoku import Sudoku
from real_word_search import Word_Search2


class Game_Manager(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.current_screen = None

    def load_page(self):
        self.root.title("Brain Games and Puzzles")
        self.current_screen = Home_page(self.root, self.word_search, self.sudoku, self.crossword)

    def word_search(self):
        self.current_screen.destroy()
        self.harry = Word_Search(self.root, self.word_search2)

    def word_search2(self, text_file):
        self.harry.destroy()
        self.albus = Word_Search2(self.root, text_file)

    def sudoku(self):
        self.current_screen.destroy()
        self.hermione = Sudoku(self.root)

    def crossword(self):
        pass

        # self.current_screen.destroy()
        # self.ron=Cross_Word


def main():
    game = Game_Manager()
    game.load_page()
    game.root.mainloop()


main()
