import tkinter
from homePage import Home_page
from wordSearch import Word_Search

class Game_Manager(object):
    def __init__(self):
        self.root = tkinter.Tk()
        self.current_screen = None

    def load_page(self):
        self.root.title("Brain Games and Puzzles")
        self.current_screen=Home_page(self.root,self.word_search, self.sudoku, self.crossword)

    def word_search(self):
        self.current_screen.destroy()
        self.harry = Word_Search(self.root)

    def sudoku(self):
        pass

    def crossword(self):
        pass


def main():
    game=Game_Manager()
    game.load_page()
    game.root.mainloop()

main()