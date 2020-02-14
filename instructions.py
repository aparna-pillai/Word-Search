from tkinter import *


class Instruction_page(Frame):
    def __init__(self, master, return_home):
        self.return_home = return_home
        super(Instruction_page, self).__init__(master)
        master.title("Instructions Page")
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.story_txt = Text(font="fixedsys 12", fg="maroon", width=100, height=18, wrap=WORD)
        self.story_txt.grid(row=0, column=0, columnspan=4)

        instructions = ("Welcome to Phoenix Puzzles: Fun Brain Games!!!\n\n"
                        "Here you can choose from three classic games: Word Search, Sudoku, and Crossword.\n\n\n"
                        "For Word Search, you can choose from three levels -- easy, medium, and hard.\n\n"
                        "When you find a word, replace all the letters of the word in the word search with an "
                        "asterisk [*]. Then press the check button to see if you've found a word!\n"
                        "Bonus! All three word searches have a theme of phoenixes and fire!\n\n"
                        "For Sudoku, you can choose from two levels and there is one crossword available to play.\n\n"
                        "When you're ready, click the 'home page' button to return to the home screen and "
                        "start your puzzle!\n\n"
                        "Can you solve them all?")

        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, instructions)

        self.home_bttn = Button(self, text="home page", command=self.back_to_home)

        Button(self, text="home",
               command=self.back_to_home,
               font="fixedsys 10",
               fg="Light Gray",
               bg="maroon"
               ).grid(row=10, column=0, sticky=W)

    def back_to_home(self):
        self.return_home()
